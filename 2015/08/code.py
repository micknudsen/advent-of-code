import codecs
import unittest


def representation_size(string: str) -> int:
    """Return the size of the string representation. This exludes
    quotes and respects escape characters."""
    return len(codecs.decode(string[1:-1], "unicode-escape"))


def memory_size(string: str) -> int:
    """Return the size of the string in memory. This includes
    both quotes and excape characters."""
    return len(string)


class TestCode(unittest.TestCase):
    def test_representation_size(self) -> None:
        self.assertEqual(representation_size(r'""'), 0)
        self.assertEqual(representation_size(r'"abc"'), 3)
        self.assertEqual(representation_size(r'"aaa\"aaa"'), 7)
        self.assertEqual(representation_size(r'"\x27"'), 1)

    def test_memory_size(self) -> None:
        self.assertEqual(memory_size(r'""'), 2)
        self.assertEqual(memory_size(r'"abc"'), 5)
        self.assertEqual(memory_size(r'"aaa\"aaa"'), 10)
        self.assertEqual(memory_size(r'"\x27"'), 6)


class TestPuzzles(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.strings = f.read().splitlines()

    def test_part_one(self) -> None:
        self.assertEqual(
            sum(
                memory_size(string) - representation_size(string)
                for string in self.strings
            ),
            1333,
        )
