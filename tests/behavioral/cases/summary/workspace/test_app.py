import unittest

from app import summarize


class SummaryTests(unittest.TestCase):
    def test_nonempty(self):
        self.assertEqual(summarize([2, 4, 6]), {"count": 3, "average": 4})


if __name__ == "__main__":
    unittest.main()
