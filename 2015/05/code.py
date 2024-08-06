import unittest


def is_nice_first_attempt(message: str) -> bool:
    """Santa has come up with a very sophisticated algorithm for determining
    whether a string is naughty or nice."""

    # Message must contain at least three vowels.
    if sum(1 for char in message if char in "aeiou") < 3:
        return False

    # Message must contain at least one letter that appears twice in a row.
    if all(message[i] != message[i + 1] for i in range(len(message) - 1)):
        return False

    # Message must not contain the strings "ab", "cd", "pq", or "xy".
    if any(
        message[i : i + 2]
        in [
            "ab",
            "cd",
            "pq",
            "xy",
        ]
        for i in range(len(message) - 1)
    ):
        return False

    return True


def is_nice_second_attempt(message: str) -> bool:
    """Realizing that the first algorithm was no good, Santa devises
    a completely new algorithm."""

    # Message must contain a pair of any two letters that appears at least
    # twice in the string without overlapping.
    if not any(message[i : i + 2] in message[i + 2 :] for i in range(len(message) - 2)):
        return False

    # Message must contain at least one letter which repeats with exactly
    # one letter between them.
    if not any(message[i] == message[i + 2] for i in range(len(message) - 2)):
        return False

    return True


class TestCode(unittest.TestCase):
    def test_is_nice_first_attempt(self) -> None:
        self.assertTrue(is_nice_first_attempt(message="ugknbfddgicrmopn"))
        self.assertTrue(is_nice_first_attempt(message="aaa"))
        self.assertFalse(is_nice_first_attempt(message="jchzalrnumimnmhp"))
        self.assertFalse(is_nice_first_attempt(message="haegwjzuvuyypxyu"))
        self.assertFalse(is_nice_first_attempt(message="dvszwmarrgswjxmb"))

    def test_is_nice_second_attempt(self) -> None:
        self.assertTrue(is_nice_second_attempt(message="qjhvhtzxzqqjkmpb"))
        self.assertTrue(is_nice_second_attempt(message="xxyxx"))
        self.assertFalse(is_nice_second_attempt(message="uurcxstgmygtbstg"))
        self.assertFalse(is_nice_second_attempt(message="ieodomkazucvgmuy"))


class TestPuzzle(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.messages = f.read().splitlines()

    def test_part_one(self) -> None:
        self.assertEqual(sum(map(is_nice_first_attempt, self.messages)), 255)

    def test_part_two(self) -> None:
        self.assertEqual(sum(map(is_nice_second_attempt, self.messages)), 55)
