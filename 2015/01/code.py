import unittest


class AdventOfCodeError(Exception):
    pass


class InvalidInstructionError(AdventOfCodeError):
    pass


class FloorNeverReachedError(AdventOfCodeError):
    pass


def deliver(instructions: str, stop: int | None = None) -> int:

    current = 0

    for count, instruction in enumerate(instructions, start=1):
        match instruction:
            case "(":
                current += 1
            case ")":
                current -= 1
            case _:
                raise InvalidInstructionError()

        if current == stop:
            return count

    if stop is not None:
        raise FloorNeverReachedError()

    return current


class TestCode(unittest.TestCase):
    def test_deliver_presents(self) -> None:
        self.assertEqual(deliver(instructions="(())"), 0)
        self.assertEqual(deliver(instructions="()()"), 0)
        self.assertEqual(deliver(instructions="((("), 3)
        self.assertEqual(deliver(instructions="(()(()("), 3)
        self.assertEqual(deliver(instructions="))((((("), 3)
        self.assertEqual(deliver(instructions="())"), -1)
        self.assertEqual(deliver(instructions="))("), -1)
        self.assertEqual(deliver(instructions=")))"), -3)
        self.assertEqual(deliver(instructions=")())())"), -3)

    def test_deliver_presents_with_stop_floor(self) -> None:
        self.assertEqual(deliver(instructions=")", stop=-1), 1)
        self.assertEqual(deliver(instructions="()())", stop=-1), 5)

    def test_deliver_presents_invalid_instruction_error(self) -> None:
        with self.assertRaises(InvalidInstructionError):
            deliver(instructions=")[(")

    def test_deliver_presents_floor_never_reached_error(self) -> None:
        with self.assertRaises(FloorNeverReachedError):
            deliver(instructions="(", stop=-1)


class TestPuzzle(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.instructions = f.read()

    def test_part_one(self) -> None:
        self.assertEqual(deliver(instructions=self.instructions), 232)

    def test_part_two(self) -> None:
        self.assertEqual(deliver(instructions=self.instructions, stop=-1), 1783)
