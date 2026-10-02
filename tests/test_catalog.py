import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

HELPER = Path(__file__).resolve().parents[1] / "skills/setup/scripts/catalog.py"


class CatalogTests(unittest.TestCase):
    def run_catalog(self, mode):
        with tempfile.TemporaryDirectory() as directory:
            server = Path(directory) / "codex"
            server.write_text(f"#!{sys.executable}\n" + '''
import json, sys, time
mode = ''' + repr(mode) + '''
initialized = False
for line in sys.stdin:
    message = json.loads(line)
    method = message['method']
    if method == 'initialized':
        initialized = True
        continue
    identifier = message['id']
    if method == 'initialize':
        result = {}
    elif method == 'model/list':
        assert initialized
        assert message['params']['includeHidden'] is False
        if mode == 'timeout':
            time.sleep(10)
        if mode == 'closed':
            break
        if mode.startswith('error'):
            error = {'code': -1}
            if mode == 'error_message':
                error['message'] = 'Sign in to Codex before listing models'
            elif mode == 'error_invalid':
                error['message'] = {'detail': 'unexpected'}
            elif mode == 'error_empty':
                error['message'] = '  '
            elif mode == 'error_shape':
                error = 'unexpected'
            print(json.dumps({'id': identifier, 'error': error}), flush=True)
            continue
        if mode == 'malformed':
            result = {'data': [{'model': 'test-model', 'supportedReasoningEfforts': [{}]}]}
        elif mode == 'empty':
            result = {'data': []}
        else:
            cursor = message['params']['cursor']
            result = {'data': [{'model': 'first' if cursor is None else 'second',
                'supportedReasoningEfforts': [{'reasoningEffort': 'high'}]}],
                'nextCursor': 'page2' if cursor is None or mode == 'cycle' else None}
    print(json.dumps({'method': 'notification'}), flush=True)
    print(json.dumps({'id': identifier, 'result': result}), flush=True)
''')
            server.chmod(0o700)
            result = subprocess.run(
                [sys.executable, str(HELPER), "--codex", str(server), "--timeout", "1"],
                text=True, capture_output=True, timeout=6,
            )
            self.assertEqual(sorted(p.name for p in Path(directory).iterdir()), ["codex"])
            return result

    def test_catalog_pagination_and_notifications(self):
        result = self.run_catalog("success")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {"models": [
            {"model": "first", "reasoningEfforts": ["high"]},
            {"model": "second", "reasoningEfforts": ["high"]},
        ]})

    def test_failures_have_no_partial_catalog(self):
        for mode in ("error", "malformed", "empty", "closed", "timeout", "cycle"):
            with self.subTest(mode=mode):
                result = self.run_catalog(mode)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertEqual(result.stdout, "")
                self.assertIn("catalog:", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_server_error_message_is_preserved(self):
        result = self.run_catalog("error_message")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr,
            "catalog: Codex rejected model/list: Sign in to Codex before listing models\n")

    def test_invalid_server_error_messages_use_safe_fallback(self):
        for mode in ("error", "error_invalid", "error_empty", "error_shape"):
            with self.subTest(mode=mode):
                result = self.run_catalog(mode)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertEqual(result.stderr, "catalog: Codex rejected model/list\n")

    def test_missing_executable(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, str(HELPER), "--codex", str(Path(directory) / "missing")],
                text=True, capture_output=True, timeout=6,
            )
        self.assertEqual(result.returncode, 2)
        self.assertIn("catalog:", result.stderr)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
