import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from behavioral.compare import collect_sessions, run_trial


class ComparisonTests(unittest.TestCase):
    def test_worker_usage_excludes_inherited_events(self):
        with tempfile.TemporaryDirectory() as directory:
            profile = Path(directory)
            sessions = profile / "sessions"
            sessions.mkdir()
            path = sessions / "worker.jsonl"
            events = [
                {"type": "session_meta", "payload": {
                    "id": "worker", "timestamp": "2026-10-07T12:00:00Z"}},
                {"timestamp": "2026-10-07T11:59:00Z", "type": "event_msg",
                 "payload": {"type": "token_count", "info": {
                     "total_token_usage": {"total_tokens": 1000}}}},
                {"timestamp": "2026-10-07T11:59:00Z", "type": "response_item",
                 "payload": {"type": "function_call", "name": "exec_command", "arguments": "{}"}},
                {"timestamp": "2026-10-07T11:59:00Z", "type": "event_msg",
                 "payload": {"type": "item_completed", "item": {"type": "CommandExecution"}}},
            ]
            path.write_text("\n".join(map(json.dumps, events)))
            result = collect_sessions(profile)[0]
            self.assertIsNone(result["usage"])
            self.assertEqual(result["tool_calls"], 0)
            self.assertEqual(result["command_actions"], 0)
            events.extend([
                {"timestamp": "2026-10-07T12:01:00Z", "type": "event_msg",
                 "payload": {"type": "token_count", "info": {
                     "total_token_usage": {"total_tokens": 50}}}},
                {"timestamp": "2026-10-07T12:01:00Z", "type": "response_item",
                 "payload": {"type": "custom_tool_call", "name": "apply_patch"}},
                {"timestamp": "2026-10-07T12:01:00Z", "type": "event_msg",
                 "payload": {"type": "item_completed", "item": {"type": "CommandExecution"}}},
            ])
            path.write_text("\n".join(map(json.dumps, events)))
            result = collect_sessions(profile)[0]
            self.assertEqual(result["usage"], {"total_tokens": 50})
            self.assertEqual(result["tool_calls"], 1)
            self.assertEqual(result["command_actions"], 1)

    def test_review_runner_uses_read_only_bundle_without_exposing_truth(self):
        from behavioral.review import consolidate
        from behavioral.compare import ROOT
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            auth = root / "source-auth"
            auth.write_text("fake test credential")
            for index, variant in enumerate(("baseline", "consolidated")):
                run = root / f"project-{index}"
                run.mkdir()
                def candidate(*args, **kwargs):
                    source = (ROOT / "skills/check/SKILL.md").read_text()
                    expected = consolidate(source) if variant == "consolidated" else source
                    self.assertEqual((run / "bundle/skills/check/SKILL.md").read_text(), expected)
                    prompt = args[0]
                    self.assertNotIn("keyword-api", prompt)
                    self.assertNotIn(variant, prompt)
                    self.assertFalse((run / "workspace/review.py").exists())
                destination = root / (variant + "-evidence")
                with patch("behavioral.compare.tempfile.mkdtemp", return_value=str(run)), \
                        patch("behavioral.compare.subprocess.Popen") as launch:
                    process = launch.return_value
                    process.communicate.side_effect = candidate
                    process.returncode = 0
                    process.poll.return_value = 0
                    result = run_trial("keyword", variant, destination, auth, "model", None, 10, "review")
                command = launch.call_args.args[0]
                self.assertEqual(command[command.index("--sandbox") + 1], "read-only")
                self.assertFalse(any("model_reasoning_effort=" in arg for arg in command))
                self.assertEqual(result["run_id"], destination.name)
                self.assertTrue(result["artifact"]["passed"])
                self.assertFalse(run.exists())

    def test_rejected_symlink_keeps_result_and_removes_credentials(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run = root / "candidate"
            run.mkdir()
            auth = root / "source-auth"
            auth.write_text("fake test credential")
            destination = root / "evidence"

            def candidate(*args, **kwargs):
                (run / "workspace/shortcut").symlink_to(root / "outside")

            with patch("behavioral.compare.tempfile.mkdtemp", return_value=str(run)), \
                    patch("behavioral.compare.subprocess.Popen") as launch, \
                    patch("behavioral.compare.assess_candidate", return_value={"passed": False}):
                process = launch.return_value
                process.communicate.side_effect = candidate
                process.returncode = 0
                process.poll.return_value = 0
                result = run_trial("exporter", "baseline", destination, auth, "model", "medium", 10)
            self.assertFalse(result["artifact"]["passed"])
            self.assertIn("snapshot_error", result["after"])
            self.assertTrue((destination / "result.json").is_file())
            self.assertTrue((destination / "workspace/shortcut").is_symlink())
            self.assertFalse(run.exists())
            self.assertEqual(auth.read_text(), "fake test credential")


if __name__ == "__main__":
    unittest.main()
