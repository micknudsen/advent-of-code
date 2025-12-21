import unittest


class InvalidInstructionError(Exception):
    pass


class FloorNeverReachedError(Exception):
    pass


def deliver_presents(instructions: str, stop_floor: int | None = None) -> int:

    current_floor = 0

    for count, instruction in enumerate(instructions, start=1):
        match instruction:
            case "(":
                current_floor += 1
            case ")":
                current_floor -= 1
            case _:
                raise InvalidInstructionError()

        if current_floor == stop_floor:
            return count

    if stop_floor is not None:
        raise FloorNeverReachedError()

    return current_floor


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
        self.assertEqual(deliver_presents(instructions=")", stop_floor=-1), 1)
        self.assertEqual(deliver_presents(instructions="()())", stop_floor=-1), 5)

    def test_deliver_presents_invalid_instruction(self) -> None:
        with self.assertRaises(InvalidInstructionError):
            deliver_presents(instructions=")[(")

    def test_deliver_presents_with_stop_floor_never_reached(self) -> None:
        with self.assertRaises(FloorNeverReachedError):
            deliver_presents(instructions="(", stop_floor=-1)


class TestPuzzle(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.instructions = f.read()

    def test_part_one(self) -> None:
        self.assertEqual(deliver_presents(instructions=self.instructions), 232)

    def test_part_two(self) -> None:
        self.assertEqual(
            deliver_presents(instructions=self.instructions, stop_floor=-1), 1783
        )
