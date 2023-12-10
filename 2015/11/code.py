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


def increment_password(password: str) -> str:
    letters = list(password[::-1])
    for i, letter in enumerate(letters):
        if letter == "z":
            letters[i] = "a"
        else:
            letters[i] = chr(ord(letter) + 1)
            break
    return "".join(letters[::-1])


def next_password(password: str) -> str:
    while True:
        password = increment_password(password)
        if is_valid(password):
            return password


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

    def test_increment_password(self) -> None:
        self.assertEqual(increment_password("xx"), "xy")
        self.assertEqual(increment_password("xy"), "xz")
        self.assertEqual(increment_password("xz"), "ya")
        self.assertEqual(increment_password("ya"), "yb")

    def test_next_password(self) -> None:
        self.assertEqual(next_password(password="abcdefgh"), "abcdffaa")
        self.assertEqual(next_password(password="ghijklmn"), "ghjaabcc")


class TestPuzzles(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.password = f.read().splitlines()[0]

    def test_part_one(self) -> None:
        self.assertEqual(next_password(self.password), "cqjxxyzz")
