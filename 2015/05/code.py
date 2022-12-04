import unittest


def is_nice(message: str) -> bool:

    if sum(1 for char in message if char in "aeiou") < 3:
        return False

    if all(message[i] != message[i + 1] for i in range(len(message) - 1)):
        return False

    if any(
        message[i : i + 2] in ["ab", "cd", "pq", "xy"]
        for i in range(len(message) - 1)
    ):
        return False

    return True


def is_very_nice(message: str) -> bool:

    if not any(
        message[i : i + 2] in message[i + 2 :] for i in range(len(message) - 2)
    ):
        return False

    if not any(message[i] == message[i + 2] for i in range(len(message) - 2)):
        return False

    return True


class TestCode(unittest.TestCase):
    def test_is_nice(self) -> None:
        self.assertTrue(is_nice(message="ugknbfddgicrmopn"))
        self.assertTrue(is_nice(message="aaa"))
        self.assertFalse(is_nice(message="jchzalrnumimnmhp"))
        self.assertFalse(is_nice(message="haegwjzuvuyypxyu"))
        self.assertFalse(is_nice(message="dvszwmarrgswjxmb"))

    def test_is_very_nice(self) -> None:
        self.assertTrue(is_very_nice(message="qjhvhtzxzqqjkmpb"))
        self.assertTrue(is_very_nice(message="xxyxx"))
        self.assertFalse(is_very_nice(message="uurcxstgmygtbstg"))
        self.assertFalse(is_very_nice(message="ieodomkazucvgmuy"))


class TestPuzzle(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.messages = f.read().splitlines()

    def test_part_one(self) -> None:
        self.assertEqual(sum(map(is_nice, self.messages)), 255)

    def test_part_two(self) -> None:
        self.assertEqual(sum(map(is_very_nice, self.messages)), 55)
