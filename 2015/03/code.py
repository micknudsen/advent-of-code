import unittest

class TestCode(unittest.TestCase):
    def test_presents_delivered(self) -> None:
        self.assertEqual(presents_delivered(directions=">"), 2)
        self.assertEqual(presents_delivered(directions="^>v<"), 4)
        self.assertEqual(presents_delivered(directions="^v^v^v^v^v"), 2)
