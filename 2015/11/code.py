import unittest


def contains_increasing_straight(password: str) -> bool:
    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i + 1]) and ord(password[i]) + 2 == ord(
            password[i + 2]
        ):
            return True
    return False


def contains_illegal_letters(password: str) -> bool:
    for letter in password:
        if letter in ["i", "o", "l"]:
            return True
    return False


class TestCode(unittest.TestCase):
    def test_contains_increasing_straight(self) -> None:
        self.assertTrue(contains_increasing_straight(password="hijklmmn"))
        self.assertFalse(contains_increasing_straight(password="abbceffg"))
        self.assertFalse(contains_increasing_straight(password="abbcegjk"))

    def test_contains_illegal_letters(self) -> None:
        self.assertTrue(contains_illegal_letters(password="hijklmmn"))
        self.assertFalse(contains_illegal_letters(password="abbceffg"))
        self.assertFalse(contains_illegal_letters(password="abbcegjk"))
