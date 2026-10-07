import json
from pathlib import Path
import tempfile
import unittest
from behavioral.traces import summarize_session, completed_workers


class TrialTraceTests(unittest.TestCase):
    def read(self, events):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'trace.jsonl'
            path.write_text('\n'.join(json.dumps(event) for event in events))
            return summarize_session(path)

    def test_completed_worker_requires_identity_verdict_and_completion(self):
        worker = self.read([
            {'type': 'session_meta', 'payload': {'id': 'child', 'parent_thread_id': 'root', 'source': {'subagent': {'thread_spawn': {'agent_path': '/root/review'}}}}},
            {'type': 'turn_context', 'payload': {'model': 'actual-model', 'effort': 'low'}},
            {'type': 'response_item', 'payload': {'type': 'message', 'role': 'assistant', 'phase': 'final_answer', 'content': [{'text': 'No findings.'}]}},
            {'type': 'event_msg', 'payload': {'type': 'task_complete'}}])
        self.assertEqual(completed_workers([worker], 'root'), [worker])
        self.assertEqual(worker['selections'], [{'model': 'actual-model', 'effort': 'low'}])
        for field, value in [('completed', False), ('verdicts', []), ('parent_id', 'other'), ('id', None), ('agent_path', None)]:
            self.assertEqual(completed_workers([dict(worker, **{field: value})], 'root'), [])

    def test_wait_or_lead_claim_does_not_establish_worker(self):
        lead = self.read([
            {'type': 'session_meta', 'payload': {'id': 'root'}},
            {'type': 'response_item', 'payload': {'type': 'function_call_output', 'call_id': 'wait', 'output': 'Wait completed.'}},
            {'type': 'response_item', 'payload': {'type': 'message', 'role': 'assistant', 'phase': 'final_answer', 'content': [{'text': 'Reviewer completed.'}]}},
            {'type': 'event_msg', 'payload': {'type': 'task_complete'}}])
        self.assertEqual(completed_workers([lead], 'root'), [])

    def test_requested_model_is_not_observed_selection(self):
        session = self.read([{'type': 'response_item', 'payload': {'type': 'function_call', 'name': 'spawn_agent', 'call_id': 'spawn', 'arguments': json.dumps({'model': 'requested', 'message': 'opaque task'})}}])
        self.assertEqual(session['selections'], [])
        self.assertEqual(session['calls'][0]['arguments'], {'model': 'requested'})

    def test_new_turn_invalidates_old_verdict(self):
        session = self.read([
            {'type': 'response_item', 'payload': {'type': 'message', 'role': 'assistant', 'phase': 'final_answer', 'content': [{'text': 'Old verdict'}]}},
            {'type': 'event_msg', 'payload': {'type': 'task_complete'}},
            {'type': 'event_msg', 'payload': {'type': 'task_started'}}])
        self.assertFalse(session['completed'])
        self.assertEqual(session['verdicts'], [])

    def test_fork_history_does_not_replace_worker_identity_or_settings(self):
        session = self.read([
            {'type': 'session_meta', 'payload': {'id': 'child', 'parent_thread_id': 'root', 'source': {'subagent': {'thread_spawn': {'agent_path': '/root/review'}}}}},
            {'type': 'session_meta', 'payload': {'id': 'root', 'source': 'exec'}},
            {'type': 'turn_context', 'payload': {'model': 'parent-model'}},
            {'type': 'event_msg', 'payload': {'type': 'task_started'}},
            {'type': 'turn_context', 'payload': {'model': 'worker-model', 'effort': 'low'}}])
        self.assertEqual(session['id'], 'child')
        self.assertEqual(session['parent_id'], 'root')
        self.assertEqual(session['selections'], [{'model': 'worker-model', 'effort': 'low'}])

    def test_inherited_completion_before_worker_creation_is_ignored(self):
        session = self.read([
            {'type': 'session_meta', 'payload': {'id': 'child', 'parent_thread_id': 'root', 'timestamp': '2026-10-07T12:00:00Z', 'source': {'subagent': {'thread_spawn': {'agent_path': '/root/review'}}}}},
            {'type': 'response_item', 'timestamp': '2026-10-07T11:59:00Z', 'payload': {'type': 'message', 'role': 'assistant', 'phase': 'final_answer', 'content': [{'text': 'Parent verdict'}]}},
            {'type': 'event_msg', 'timestamp': '2026-10-07T11:59:01Z', 'payload': {'type': 'task_complete'}}])
        self.assertEqual(completed_workers([session], 'root'), [])
