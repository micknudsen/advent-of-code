import unittest

from dataclasses import dataclass
from typing import Iterable


class InvalidDirectionError(Exception):
    def __init__(self, direction: str) -> None:
        self.message = f"Invalid direction: {direction}"
        super().__init__(self.message)


@dataclass
class House:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash((self.x, self.y))


def presents_delivered(directions: Iterable[str]) -> int:

    current: House = House(x=0, y=0)
    visited: set[House] = {current}

    for direction in directions:
        if direction == "^":
            current = House(current.x, current.y + 1)
        elif direction == "v":
            current = House(current.x, current.y - 1)
        elif direction == ">":
            current = House(current.x + 1, current.y)
        elif direction == "<":
            current = House(current.x - 1, current.y)
        else:
            raise InvalidDirectionError(direction)

        visited.add(current)

    return len(visited)


class TestCode(unittest.TestCase):
    def test_house_equality(self):
        self.assertEqual(House(x=1, y=1), House(x=1, y=1))
        self.assertNotEqual(House(x=1, y=1), House(x=1, y=2))

    def test_presents_delivered(self) -> None:
        self.assertEqual(presents_delivered(directions=">"), 2)
        self.assertEqual(presents_delivered(directions="^>v<"), 4)
        self.assertEqual(presents_delivered(directions="^v^v^v^v^v"), 2)

    def test_present_delivered_with_invalid_direction(self) -> None:
        with self.assertRaises(InvalidDirectionError):
            presents_delivered(directions="x")


class TestPuzzle(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.directions = f.read()

    def test_part_one(self) -> None:
        self.assertEqual(presents_delivered(directions=self.directions), 2565)
