import unittest

from app import export_invoice


class ExportTests(unittest.TestCase):
    def test_export(self):
        self.assertEqual(export_invoice(19.5), {"amount": 19.5})


if __name__ == "__main__":
    unittest.main()
