import unittest


class TestCode(unittest.TestCase):
    def test_is_valid(self) -> None:
        self.assertFalse(is_valid(password="hijklmmn"))
        self.assertFalse(is_valid(password="abbceffg"))
        self.assertFalse(is_valid(password="abbcegjk"))

    def test_next_password(self) -> None:
        self.assertEqual(next_password(password="abcdefgh"), "abcdffaa")
        self.assertEqual(next_password(password="ghijklmn"), "ghjaabcc")
