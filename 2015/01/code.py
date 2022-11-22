import unittest

from typing import Iterable, Optional


class InvalidInstructionError(Exception):
    def __init__(self, instruction: str) -> None:
        self.message = f"Invalid instruction: {instruction}"
        super().__init__(self.message)


class FloorNeverReachedError(Exception):
    def __init__(self, floor: int) -> None:
        self.message = f"Never reached floor {floor}"
        super().__init__(self.message)


def deliver_presents(
    instructions: Iterable[str], stop_at_floor: Optional[int] = None
) -> int:
    """Santa delivers presents starting at floor `0` based on `instructions`
    given as a sequence of characters. Here `(` (resp. `)`) means go one floor
    up (resp. down). Any other instruction raises an exception.

    If `stop_at_floor` is specified, Santa stops when reaching that floor,
    and the total floor count is returned. If the floor is never reached, an
    exception is raised. If `stop_at_floor` is not specified, the function
    returns the final floor reached after following all `instructions`."""
    floor = 0
    for count, instruction in enumerate(instructions, start=1):
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1
        else:
            raise InvalidInstructionError(instruction=instruction)
        if floor == stop_at_floor:
            return count
    if stop_at_floor is not None:
        raise FloorNeverReachedError(floor=stop_at_floor)
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

    def test_deliver_presents_with_stop_floor_never_reached(self) -> None:
        with self.assertRaises(FloorNeverReachedError):
            deliver_presents(instructions="(", stop_at_floor=-1)


class TestPuzzle(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.instructions = f.read()

    def test_part_one(self) -> None:
        self.assertEqual(deliver_presents(instructions=self.instructions), 232)

    def test_part_two(self) -> None:
        self.assertEqual(
            deliver_presents(instructions=self.instructions, stop_at_floor=-1),
            1783,
        )
