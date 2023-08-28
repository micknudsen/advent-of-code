import unittest


def say(number: str) -> str:
    result = ""

    digit = number[0]
    count = 1

    for next_digit in number[1:]:
        if next_digit == digit:
            count += 1
        else:
            result += f"{count}{digit}"
            digit = next_digit
            count = 1

    result = result + f"{count}{digit}"
    return result


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
        self.assertEqual(
            len(solution),
            492982,
        )

    def test_part_two(self) -> None:
        solution = self.number
        for _ in range(50):
            solution = say(solution)
        self.assertEqual(
            len(solution),
            6989950,
        )
