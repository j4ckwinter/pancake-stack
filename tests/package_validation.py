"""Read-only checks for this repository's package conventions, not a schema validator.

Skill headers support only plain, unquoted, single-line name and description.
Header values begin with an ASCII letter; YAML scalar literals are unsupported.
Markdown checks cover relative inline links, not reference-style links or anchors.
"""

import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
SEMVER = re.compile(
    r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)"
    r"(?:-(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)(?:\.(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*))*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?\Z"
)
LINK = re.compile(r"\[[^\]\n]*\]\((<[^>\n]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)")
SCALAR_LITERALS = {"true", "false", "yes", "no", "on", "off", "null"}


def validate_package(root: Path) -> list[str]:
    """Return file-specific diagnostics without modifying files or invoking hosts."""
    root = root.resolve()
    errors = []

    def fail(path, message):
        errors.append(f"{path.relative_to(root)}: {message}")

    def read(path):
        if not path.resolve().is_relative_to(root):
            fail(path, "path escapes package")
            return None
        try:
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            fail(path, f"cannot read file ({error})")
            return None

    def json_object(path):
        source = read(path)
        if source is None:
            return {}

        def pairs(items):
            result = {}
            for key, value in items:
                if key in result:
                    raise ValueError(f"duplicate JSON key {key!r}")
                result[key] = value
            return result

        def reject_constant(value):
            raise ValueError(f"invalid JSON constant {value}")

        try:
            result = json.loads(source, object_pairs_hook=pairs, parse_constant=reject_constant)
            if not isinstance(result, dict):
                raise ValueError("expected JSON object")
            return result
        except ValueError as error:
            fail(path, f"invalid JSON ({error})")
            return {}

    def nonempty(value):
        return isinstance(value, str) and bool(value.strip())

    manifest_path = root / "plugin.json"
    manifest = json_object(manifest_path)
    name = manifest.get("name")
    if manifest.get("$schema") != SCHEMA:
        fail(manifest_path, "expected declared portable schema URL")
    if not isinstance(name, str) or not NAME.fullmatch(name):
        fail(manifest_path, "name must be a lowercase hyphenated identifier")
    if not nonempty(manifest.get("description")):
        fail(manifest_path, "description must be a nonempty string")
    version = manifest.get("version")
    if not isinstance(version, str) or not SEMVER.fullmatch(version):
        fail(manifest_path, "version must be semantic version text")
    author = manifest.get("author")
    if not isinstance(author, dict) or not nonempty(author.get("name")):
        fail(manifest_path, "author must be an object with a nonempty name")
    extensions = manifest.get("extensions")
    openai = extensions.get("com.openai") if isinstance(extensions, dict) else None
    interface = openai.get("interface") if isinstance(openai, dict) else None
    if not isinstance(interface, dict):
        fail(manifest_path, "extensions.com.openai.interface must be an object")
    else:
        for field in ("displayName", "shortDescription", "developerName", "category"):
            if not nonempty(interface.get(field)):
                fail(manifest_path, f"interface.{field} must be a nonempty string")

    marketplace_path = root / ".agents/plugins/marketplace.json"
    marketplace = json_object(marketplace_path)
    entries = marketplace.get("plugins")
    if not isinstance(entries, list) or len(entries) != 1 or not isinstance(entries[0], dict):
        fail(marketplace_path, "expected one local package entry")
    else:
        entry = entries[0]
        if entry.get("name") != name:
            fail(marketplace_path, "plugin entry name must match plugin.json")
        source = entry.get("source")
        if not isinstance(source, dict) or source.get("source") != "local" or source.get("path") != "./":
            fail(marketplace_path, "package source must be local ./")
        elif (root / source["path"]).resolve() != root:
            fail(marketplace_path, "local source does not resolve to package root")

    for path in sorted((root / "config").glob("*.example.json")):
        json_object(path)

    skills = set()
    for path in sorted((root / "skills").glob("*/SKILL.md")):
        directory = path.parent
        text = read(path)
        skills.add(directory.name)
        if text is None:
            continue
        lines = text.splitlines()
        if not lines or lines[0] != "---" or "---" not in lines[1:]:
            fail(path, "missing delimited frontmatter")
            continue
        fields = {}
        for line in lines[1:lines.index("---", 1)]:
            match = re.fullmatch(r"(name|description): (\S.*)", line)
            if (not match or not re.match(r"[A-Za-z]", match[2])
                    or match[2].strip().lower() in SCALAR_LITERALS
                    or re.search(r":(?:\s|$)|\s#", match[2])):
                fail(path, "unsupported frontmatter; use plain unquoted single-line name and description")
                continue
            key, value = match.groups()
            if key in fields:
                fail(path, f"duplicate frontmatter field {key}")
            fields[key] = value
        if fields.get("name") != directory.name or not NAME.fullmatch(fields.get("name", "")) or len(fields.get("name", "")) > 64:
            fail(path, "name must match directory and be a lowercase identifier of at most 64 characters")
        if not fields.get("description", "").strip() or len(fields.get("description", "")) > 1024:
            fail(path, "description must contain 1 to 1024 characters")

    readme_path = root / "README.md"
    readme = read(readme_path)
    if readme is not None and isinstance(name, str):
        mentioned = set(re.findall(r"\$" + re.escape(name) + r":([a-z0-9-]+)", readme))
        for missing in sorted(skills - mentioned):
            fail(readme_path, f"missing documented skill {missing}")
        for extra in sorted(mentioned - skills):
            fail(readme_path, f"unknown documented skill {extra}")

    documents = [readme_path, *sorted((root / "docs").rglob("*.md")), *sorted((root / "skills").rglob("*.md"))]
    for path in documents:
        source = read(path)
        if source is None:
            continue
        for match in LINK.finditer(source):
            target = match[1].strip("<>")
            try:
                parsed = urlsplit(target)
            except ValueError:
                fail(path, f"invalid inline link target: {target}")
                continue
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(root):
                fail(path, f"relative link escapes package: {target}")
            elif not destination.exists():
                fail(path, f"missing relative link target: {target}")
    return errors
