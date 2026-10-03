import json
from pathlib import Path
import unittest

import archive
import consumer
from producer import create_invoice


class RecordTests(unittest.TestCase):
    def test_live(self):
        payload = create_invoice(19.5)
        self.assertEqual(payload, {"total": 19.5})
        self.assertEqual(consumer.read_total(payload), 19.5)

    def test_archive(self):
        records = json.loads(Path(__file__).with_name("archive.json").read_text())
        self.assertEqual(archive.read_total(records[0]), 19.5)


if __name__ == "__main__":
    unittest.main()
