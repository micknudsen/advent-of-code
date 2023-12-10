import unittest

from itertools import groupby


def say(number: str) -> str:
    """Implementation of the look-and-say function. That is, the output is the number
    obtained by reading the input number out loud, grouping identical digits together.
    For example, reading 21 out loud is "one two, one one", which is 1211."""
    return "".join(f"{len(list(group))}{digit}" for digit, group in groupby(number))


class TestCode(unittest.TestCase):
    def test_say(self) -> None:
        self.assertEqual(say(number="1"), "11")
        self.assertEqual(say(number="11"), "21")
        self.assertEqual(say(number="21"), "1211")
        self.assertEqual(say(number="1211"), "111221")
        self.assertEqual(say(number="111221"), "312211")


class TestPuzzles(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.number = f.read().splitlines()[0]

    def test_part_one(self) -> None:
        solution = self.number
        for _ in range(40):
            solution = say(solution)
        self.assertEqual(len(solution), 492982)

    def test_part_two(self) -> None:
        solution = self.number
        for _ in range(50):
            solution = say(solution)
        self.assertEqual(len(solution), 6989950)
