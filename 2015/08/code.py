import ast
import unittest


def overhead(string: str) -> int:
    """Every line on Santa's list is enclosed by double quotes and
    maybe contain some escaped characters. This function computes the
    overhead memory used for storing all this things compared to the
    bare string literal itself."""
    return len(string) - len(ast.literal_eval(string))


def increase(string: str) -> int:
    """Every entry on Santa's list must now be further encoded. This
    means enclosing the string literal in double quotes and escaping
    quotes and backslashes inside the string itself. This function
    computes the increase in memory usage for storing all these things."""
    return 2 + string.count('"') + string.count("\\")


class TestCode(unittest.TestCase):
    def test_overhead(self) -> None:
        self.assertEqual(overhead(string=r'""'), 2)
        self.assertEqual(overhead(string=r'"abc"'), 2)
        self.assertEqual(overhead(string=r'"aaa\"aaa"'), 3)
        self.assertEqual(overhead(string=r'"\x27"'), 5)

    def test_increase(self) -> None:
        self.assertEqual(increase(string=r'""'), 4)
        self.assertEqual(increase(string=r'"abc"'), 4)
        self.assertEqual(increase(string=r'"aaa\"aaa"'), 6)
        self.assertEqual(increase(string=r'"\x27"'), 5)


class TestPuzzles(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.strings = f.read().splitlines()

    def test_part_one(self) -> None:
        self.assertEqual(sum(map(overhead, self.strings)), 1333)

    def test_part_two(self) -> None:
        self.assertEqual(sum(map(increase, self.strings)), 2046)
