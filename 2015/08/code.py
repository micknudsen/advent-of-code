import codecs
import unittest


def literal(string: str) -> str:
    """Return the string literal including
    quotes and escape characters."""
    return codecs.decode(string[1:-1], "unicode-escape")


class TestCode(unittest.TestCase):
    def test_literal(self) -> None:
        self.assertEqual(literal(r'""'), r"")
        self.assertEqual(literal(r'"abc"'), r"abc")
        self.assertEqual(literal(r'"aaa\"aaa"'), r'aaa"aaa')
        self.assertEqual(literal(r'"\x27"'), r"'")


class TestPuzzles(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.strings = f.read().splitlines()

    def test_part_one(self) -> None:
        self.assertEqual(
            sum(len(string) - len(literal(string)) for string in self.strings),
            1333,
        )
