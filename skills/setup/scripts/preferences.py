#!/usr/bin/env python3
"""Store Pancake Stack preferences without modifying Codex settings."""

import argparse
import json
import os
from pathlib import Path
import sys
import tempfile

ROLES = ("implementation", "review", "research")
FIELDS = ("model", "reasoningEffort")


def empty_config():
    return {
        "schemaVersion": 1,
        "defaults": dict.fromkeys(FIELDS),
        "roles": {role: dict.fromkeys(FIELDS) for role in ROLES},
    }


def exact_keys(value, keys, label):
    if not isinstance(value, dict) or set(value) != set(keys):
        raise ValueError(f"{label} must contain exactly {', '.join(keys)}")


def validate(config):
    if not isinstance(config, dict):
        raise ValueError("preferences must be an object")
    version = config.get("schemaVersion")
    if type(version) is not int or version not in (1, 2):
        raise ValueError("schemaVersion must be the integer 1 or 2")
    keys = ("schemaVersion", "defaults", "roles")
    if version == 2:
        keys += ("challengeReviewers",)
    exact_keys(config, keys, "preferences")
    exact_keys(config["roles"], ROLES, "roles")
    choices = [("defaults", config["defaults"])]
    choices.extend((role, config["roles"][role]) for role in ROLES)
    if version == 2:
        reviewers = config["challengeReviewers"]
        if not isinstance(reviewers, list):
            raise ValueError("challengeReviewers must be a list")
        choices.extend((f"challengeReviewers[{index}]", choice)
                       for index, choice in enumerate(reviewers))
    for label, choice in choices:
        exact_keys(choice, FIELDS, label)
        for field, value in choice.items():
            if value is not None and (
                not isinstance(value, str) or not value.strip() or value != value.strip()
            ):
                raise ValueError(f"{label}.{field} must be null or a nonempty trimmed string")
    return config


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key}")
        result[key] = value
    return result


def parse(text):
    try:
        return validate(json.loads(text, object_pairs_hook=unique_object))
    except json.JSONDecodeError as error:
        raise ValueError(f"invalid JSON at line {error.lineno}, column {error.colno}") from error


def read_config(path):
    try:
        content = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return empty_config()
    return parse(content)


def save_config(path, config):
    read_config(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent, delete=False
        ) as output:
            temporary = Path(output.name)
            output.write(json.dumps(config, indent=2) + "\n")
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def resolve(config, host_model, host_effort):
    host = {"model": host_model, "reasoningEffort": host_effort}
    effective = {}
    for role in ROLES:
        effective[role] = {}
        for field in FIELDS:
            value = config["roles"][role][field]
            if value is None:
                value = config["defaults"][field]
            if value is None:
                value = host[field]
            effective[role][field] = value
    return effective


def resolve_challenge(config, host_model, host_effort):
    review = resolve(config, host_model, host_effort)["review"]
    reviewers = config.get("challengeReviewers") or [dict.fromkeys(FIELDS)]
    return [
        {field: review[field] if choice[field] is None else choice[field]
         for field in FIELDS}
        for choice in reviewers
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, help="override the preference file path")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("show")
    commands.add_parser("save", help="validate and save the complete JSON object from stdin")
    for command in ("resolve", "resolve-challenge"):
        resolver = commands.add_parser(command)
        resolver.add_argument("--host-model")
        resolver.add_argument("--host-reasoning-effort")
    args = parser.parse_args()
    try:
        codex_home = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
        path = args.config if args.config is not None else codex_home / "pancake-stack/config.json"
        if args.command == "save":
            result = parse(sys.stdin.read())
            save_config(path, result)
        else:
            result = read_config(path)
            if args.command in ("resolve", "resolve-challenge"):
                host = empty_config()
                host["defaults"] = {
                    "model": args.host_model,
                    "reasoningEffort": args.host_reasoning_effort,
                }
                validate(host)
                resolver = resolve_challenge if args.command == "resolve-challenge" else resolve
                result = resolver(result, args.host_model, args.host_reasoning_effort)
        print(json.dumps(result, indent=2))
    except (ValueError, OSError, UnicodeError) as error:
        print(f"preferences: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
