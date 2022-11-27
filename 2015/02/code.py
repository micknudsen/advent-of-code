import unittest


class TestCode(unittest.TestCase):
    def test_paper_needed(self) -> None:
        self.assertEqual(paper_needed(lenght=2, width=3, height=4), 58)
        self.assertEqual(paper_needed(lenght=1, width=1, height=10), 43)
