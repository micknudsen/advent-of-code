import unittest

from typing import Iterable


class InvalidInstructionError(Exception):
    def __init__(self, instruction: str) -> None:
        self.message = f"Invalid instruction: {instruction}"
        super().__init__(self.message)


def deliver_presents(instructions: Iterable[str]) -> int:
    """Santa delivers presents starting at floor 0 based on `instructions`
    given as a sequence of characters. Here "(" (resp. ")") means go one floor
    up (resp. down). Any other instruction raises an exception. Return the
    final floor number."""

    floor = 0
    for instruction in instructions:
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1
        else:
            raise InvalidInstructionError(instruction=instruction)
    return floor


class TestCode(unittest.TestCase):
    def test_deliver_presents(self) -> None:
        self.assertEqual(deliver_presents(instructions="(())"), 0)
        self.assertEqual(deliver_presents(instructions="()()"), 0)
        self.assertEqual(deliver_presents(instructions="((("), 3)
        self.assertEqual(deliver_presents(instructions="(()(()("), 3)
        self.assertEqual(deliver_presents(instructions="))((((("), 3)
        self.assertEqual(deliver_presents(instructions="())"), -1)
        self.assertEqual(deliver_presents(instructions="))("), -1)
        self.assertEqual(deliver_presents(instructions=")))"), -3)
        self.assertEqual(deliver_presents(instructions=")())())"), -3)

    def test_deliver_presents_with_stop(self) -> None:
        self.assertEqual(
            deliver_presents(instructions=")", stop_at_floor=-1), 1
        )
        self.assertEqual(
            deliver_presents(instructions="()())", stop_at_floor=-1), 5
        )

    def test_deliver_presents_invalid_instruction(self) -> None:
        with self.assertRaises(InvalidInstructionError):
            deliver_presents(instructions=")[(")


class TestPuzzle(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.instructions = f.read()

    def test_part_one(self) -> None:
        self.assertEqual(deliver_presents(instructions=self.instructions), 232)
