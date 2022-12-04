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


class TestCode(unittest.TestCase):
    def test_is_nice(self) -> None:
        self.assertTrue(is_nice(message="ugknbfddgicrmopn"))
        self.assertTrue(is_nice(message="aaa"))
        self.assertFalse(is_nice(message="jchzalrnumimnmhp"))
        self.assertFalse(is_nice(message="haegwjzuvuyypxyu"))
        self.assertFalse(is_nice(message="dvszwmarrgswjxmb"))
