import unittest

from typing import Set


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


def contains_two_pairs(password: str) -> bool:
    pairs: Set[str] = set()
    for x, y in zip(password, password[1:]):
        if x == y:
            pairs.add(x)
            if len(pairs) == 2:
                return True
    return False


def is_valid(password: str) -> bool:
    return all(
        [
            contains_increasing_straight(password),
            not contains_illegal_letters(password),
            contains_two_pairs(password),
        ]
    )


class TestCode(unittest.TestCase):
    def test_contains_increasing_straight(self) -> None:
        self.assertTrue(contains_increasing_straight(password="hijklmmn"))
        self.assertFalse(contains_increasing_straight(password="abbceffg"))
        self.assertFalse(contains_increasing_straight(password="abbcegjk"))

    def test_contains_illegal_letters(self) -> None:
        self.assertTrue(contains_illegal_letters(password="hijklmmn"))
        self.assertFalse(contains_illegal_letters(password="abbceffg"))
        self.assertFalse(contains_illegal_letters(password="abbcegjk"))

    def test_contains_two_pairs(self) -> None:
        self.assertFalse(contains_two_pairs(password="hijklmmn"))
        self.assertTrue(contains_two_pairs(password="abbceffg"))
        self.assertFalse(contains_two_pairs(password="abbcegjk"))

    def test_is_valid(self) -> None:
        self.assertFalse(is_valid(password="hijklmmn"))
        self.assertFalse(is_valid(password="abbceffg"))
        self.assertFalse(is_valid(password="abbcegjk"))
        self.assertTrue(is_valid(password="abcdffaa"))
        self.assertTrue(is_valid(password="ghjaabcc"))
