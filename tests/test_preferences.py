import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "skills/setup/scripts/preferences.py"
EXAMPLE = json.loads((ROOT / "config/preferences.example.json").read_text())


class PreferencesTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "nested/config.json"

    def run_cli(self, command, payload=None, *args):
        return subprocess.run(
            [sys.executable, str(HELPER), "--config", str(self.path), command, *args],
            input=payload, text=True, capture_output=True,
        )

    def test_missing_show_and_resolution_do_not_write(self):
        result = self.run_cli("show")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), EXAMPLE)
        result = self.run_cli("resolve")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {
            "implementation": {"model": None, "reasoningEffort": None},
            "review": {"model": None, "reasoningEffort": None},
            "research": {"model": None, "reasoningEffort": None},
        })
        self.assertFalse(self.path.parent.exists())

    def test_save_round_trip_and_repeat(self):
        config = copy.deepcopy(EXAMPLE)
        config["defaults"]["model"] = "host-model"
        for _ in range(2):
            result = self.run_cli("save", json.dumps(config))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout), config)
            self.assertEqual(json.loads(self.path.read_text()), config)
        self.assertEqual(json.loads(self.run_cli("show").stdout), config)
        self.assertEqual(list(self.path.parent.iterdir()), [self.path])

    def test_mixed_inheritance(self):
        config = copy.deepcopy(EXAMPLE)
        config["defaults"]["reasoningEffort"] = "high"
        config["roles"]["review"]["model"] = "review-model"
        config["roles"]["research"]["reasoningEffort"] = "medium"
        self.assertEqual(self.run_cli("save", json.dumps(config)).returncode, 0)
        result = self.run_cli("resolve", None, "--host-model", "parent-model",
                              "--host-reasoning-effort", "low")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {
            "implementation": {"model": "parent-model", "reasoningEffort": "high"},
            "review": {"model": "review-model", "reasoningEffort": "high"},
            "research": {"model": "parent-model", "reasoningEffort": "medium"},
        })
        self.assertEqual(self.run_cli("save", json.dumps(EXAMPLE)).returncode, 0)
        result = self.run_cli("resolve", None, "--host-model", "parent-model",
                              "--host-reasoning-effort", "low")
        self.assertEqual(json.loads(result.stdout), {
            role: {"model": "parent-model", "reasoningEffort": "low"}
            for role in ("implementation", "review", "research")
        })

    def test_invalid_inputs_preserve_existing_file(self):
        self.assertEqual(self.run_cli("save", json.dumps(EXAMPLE)).returncode, 0)
        original = self.path.read_bytes()
        invalid = ["{", "[]", '{"schemaVersion":1,"schemaVersion":1}']
        for version in (True, 2, "1", 1.0):
            config = copy.deepcopy(EXAMPLE)
            config["schemaVersion"] = version
            invalid.append(json.dumps(config))
        for location in ((), ("defaults",), ("roles",), ("roles", "review")):
            for mutation in ("extra", "missing"):
                config = copy.deepcopy(EXAMPLE)
                target = config
                for key in location:
                    target = target[key]
                if mutation == "extra":
                    target["extra"] = None
                else:
                    del target[next(iter(target))]
                invalid.append(json.dumps(config))
        for value in ("", " ", " model", "model ", False, 3, [], {}):
            config = copy.deepcopy(EXAMPLE)
            config["defaults"]["model"] = value
            invalid.append(json.dumps(config))
        for payload in invalid:
            with self.subTest(payload=payload):
                result = self.run_cli("save", payload)
                self.assertEqual(result.returncode, 2)
                self.assertNotIn("Traceback", result.stderr)
                self.assertEqual(self.path.read_bytes(), original)

    def test_corrupt_or_future_existing_file_is_not_overwritten(self):
        self.path.parent.mkdir()
        future = copy.deepcopy(EXAMPLE)
        future["schemaVersion"] = 2
        for payload in ("{", json.dumps(future)):
            self.path.write_text(payload)
            for command in ("show", "save"):
                result = self.run_cli(command, json.dumps(EXAMPLE))
                self.assertEqual(result.returncode, 2)
                self.assertEqual(self.path.read_text(), payload)

    def test_filesystem_error_has_no_traceback(self):
        self.path.parent.write_text("parent is a file")
        result = self.run_cli("save", json.dumps(EXAMPLE))
        self.assertEqual(result.returncode, 2)
        self.assertNotIn("Traceback", result.stderr)
        self.assertEqual(self.path.parent.read_text(), "parent is a file")


if __name__ == "__main__":
    unittest.main()
