import ast
import unittest


def overhead(string: str) -> int:
    return len(string) - len(ast.literal_eval(string))


class TestCode(unittest.TestCase):
    def test_overhead(self) -> None:
        self.assertEqual(
            overhead(string=r'""'),
            2,
        )
        self.assertEqual(
            overhead(string=r'"abc"'),
            2,
        )
        self.assertEqual(
            overhead(string=r'"aaa\"aaa"'),
            3,
        )
        self.assertEqual(
            overhead(string=r'"\x27"'),
            5,
        )

    def test_increase(self) -> None:
        self.assertEqual(
            increase(string=r'""'),
            4,
        )
        self.assertEqual(
            increase(string=r'"abc"'),
            4,
        )
        self.assertEqual(
            increase(string=r'"aaa\"aaa"'),
            6,
        )
        self.assertEqual(
            increase(string=r'"\x27"'),
            5,
        )


class TestPuzzles(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.strings = f.read().splitlines()

    def test_part_one(self) -> None:
        self.assertEqual(
            sum(map(overhead, self.strings)),
            1333,
        )
