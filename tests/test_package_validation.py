import json
from pathlib import Path
import shutil
import tempfile
import unittest

from package_validation import validate_package

ROOT = Path(__file__).resolve().parents[1]


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.storage = tempfile.TemporaryDirectory()
        self.addCleanup(self.storage.cleanup)
        self.root = Path(self.storage.name) / "package"
        self.root.mkdir()
        for directory in ("skills", "docs", "config", ".agents", ".claude-plugin", "tests/behavioral/cases"):
            shutil.copytree(ROOT / directory, self.root / directory)
        for filename in ("README.md", "plugin.json"):
            shutil.copy2(ROOT / filename, self.root / filename)

    def edit_json(self, filename, change):
        path = self.root / filename
        data = json.loads(path.read_text())
        change(data)
        path.write_text(json.dumps(data))

    def assert_diagnostic(self, filename, text):
        self.assertTrue(any(message.startswith(filename + ":") and text in message
                            for message in validate_package(self.root)), validate_package(self.root))

    def test_real_repository_passes(self):
        self.assertEqual(validate_package(ROOT), [])

    def test_validation_leaves_package_unchanged(self):
        before = {path.relative_to(self.root): path.read_bytes()
                  for path in self.root.rglob("*") if path.is_file()}
        self.assertEqual(validate_package(self.root), [])
        after = {path.relative_to(self.root): path.read_bytes()
                 for path in self.root.rglob("*") if path.is_file()}
        self.assertEqual(after, before)

    def test_supported_changes_pass(self):
        for filename in ("plugin.json", ".claude-plugin/plugin.json"):
            self.edit_json(filename, lambda data: data.update(version="1.2.3-rc.1+build.2", description="Different useful description"))
        self.edit_json(".claude-plugin/marketplace.json", lambda data: data["plugins"][0].update(version="1.2.3-rc.1+build.2", description="Different useful description"))
        self.edit_json(".claude-plugin/marketplace.json", lambda data: data["metadata"].update(description="Different useful description"))
        path = self.root / "README.md"
        path.write_text(path.read_text() + "\nRepeat `$pancake-stack:fix`. [Directory](skills/) [fragment](#here) [encoded](docs/%72ecipes.md)\n")
        self.assertEqual(validate_package(self.root), [])

    def test_invalid_json_and_duplicates(self):
        for filename, content, expected in (
            ("plugin.json", "{", "invalid JSON"),
            (".agents/plugins/marketplace.json", '{"plugins":[],"plugins":[]}', "duplicate JSON key"),
            ("config/preferences.example.json", '{"defaults":{"model":null,"model":null}}', "duplicate JSON key"),
        ):
            with self.subTest(filename=filename):
                (self.root / filename).write_text(content)
                self.assert_diagnostic(filename, expected)

    def test_marketplace_identity_and_source(self):
        filename = ".agents/plugins/marketplace.json"
        self.edit_json(filename, lambda data: data["plugins"][0].update(name="other"))
        self.assert_diagnostic(filename, "name must match")
        self.edit_json(filename, lambda data: data["plugins"][0]["source"].update(path="../"))
        self.assert_diagnostic(filename, "source must be local ./")

    def test_invalid_manifest_shapes(self):
        for field, value, expected in (("version", "01.2.3", "semantic version"), ("description", " ", "nonempty"), ("author", [], "author must"), ("extensions", [], "interface must"), ("$schema", "other", "schema URL")):
            with self.subTest(field=field):
                original = (self.root / "plugin.json").read_text()
                self.edit_json("plugin.json", lambda data: data.update({field: value}))
                self.assert_diagnostic("plugin.json", expected)
                (self.root / "plugin.json").write_text(original)

    def test_claude_contracts_and_metadata_drift(self):
        cases = (
            (".claude-plugin/plugin.json", lambda data: data.update(skills="../skills"), "shared ./skills/"),
            (".claude-plugin/plugin.json", lambda data: data.update(version="0.0.0"), "version must match"),
            (".claude-plugin/plugin.json", lambda data: data.update(hooks={}), "native Claude manifest fields"),
            (".claude-plugin/marketplace.json", lambda data: data["plugins"][0].update(source="../"), "source must be ./"),
            (".claude-plugin/marketplace.json", lambda data: data["plugins"][0].update(description="drift"), "description must match"),
            (".claude-plugin/marketplace.json", lambda data: data.update(owner={"name": "other"}), "owner must match"),
            (".claude-plugin/marketplace.json", lambda data: data.update(plugins=[]), "one local package entry"),
            (".claude-plugin/marketplace.json", lambda data: data.update(metadata={}), "marketplace description must match"),
        )
        for filename, change, expected in cases:
            with self.subTest(filename=filename, expected=expected):
                path = self.root / filename
                original = path.read_text()
                self.edit_json(filename, change)
                self.assert_diagnostic(filename, expected)
                path.write_text(original)
        for filename in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"):
            path = self.root / filename
            original = path.read_text()
            path.write_text('{"name":"a","name":"b"}')
            self.assert_diagnostic(filename, "duplicate JSON key")
            path.write_text(original)

    def test_skill_frontmatter_and_missing_file(self):
        filename = "skills/fix/SKILL.md"
        path = self.root / filename
        for header, expected in (("name: other\ndescription: text", "name must match"), ("name: fix\nname: fix\ndescription: text", "duplicate frontmatter"), ("name: fix\ndescription: |\n  text", "unsupported frontmatter"), ("name: fix\ndescription: \"text\"", "unsupported frontmatter"), ("name: fix\ndescription: " + "a" * 1025, "1 to 1024")):
            with self.subTest(expected=expected):
                path.write_text("---\n" + header + "\n---\n")
                self.assert_diagnostic(filename, expected)
        path.unlink()
        self.assert_diagnostic("README.md", "unknown documented skill fix")

    def test_readme_skill_coverage(self):
        path = self.root / "README.md"
        path.write_text(path.read_text().replace("$pancake-stack:fix", "$pancake-stack:unknown"))
        self.assert_diagnostic("README.md", "missing documented skill fix")
        self.assert_diagnostic("README.md", "unknown documented skill unknown")

    def test_yaml_syntax_and_non_string_scalars_are_rejected(self):
        filename = "skills/fix/SKILL.md"
        for value in ("true", "NO", "null", "123", "2026-10-03", "text: more", "text:", "# comment", "text\t# comment", "&anchor text", "!tag text"):
            with self.subTest(value=value):
                (self.root / filename).write_text("---\nname: fix\ndescription: " + value + "\n---\n")
                self.assert_diagnostic(filename, "unsupported frontmatter")

    def test_missing_and_escaping_references(self):
        path = self.root / "skills/fix/SKILL.md"
        path.write_text(path.read_text() + "\n[Missing](missing.md) [Escaping](../../../outside.md)\n")
        self.assert_diagnostic("skills/fix/SKILL.md", "missing relative link")
        self.assert_diagnostic("skills/fix/SKILL.md", "escapes package")

    def test_symlink_reference_escape(self):
        (self.root / "docs/external.md").symlink_to(Path(self.storage.name) / "outside.md")
        path = self.root / "README.md"
        path.write_text(path.read_text() + "\n[Outside](docs/external.md)\n")
        self.assert_diagnostic("README.md", "escapes package")


if __name__ == "__main__":
    unittest.main()
