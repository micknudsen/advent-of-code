import unittest


class TestCode(unittest.TestCase):
    def test_contains_increasing_straight(self) -> None:
        self.assertTrue(contains_increasing_straight(password="hijklmmn"))
        self.assertFalse(contains_increasing_straight(password="abbceffg"))
        self.assertFalse(contains_increasing_straight(password="abbcegjk"))
