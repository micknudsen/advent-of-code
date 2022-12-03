import unittest


class TestCode(unittest.TestCase):
    def test_is_nice(self) -> None:
        self.assertTrue(is_nice(message="ugknbfddgicrmopn"))
        self.assertTrue(is_nice(message="aaa"))
        self.assertFalse(is_nice(message="jchzalrnumimnmhp"))
        self.assertFalse(is_nice(message="haegwjzuvuyypxyu"))
        self.assertFalse(is_nice(message="dvszwmarrgswjxmb"))
