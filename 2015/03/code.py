import unittest

from dataclasses import dataclass
from typing import Iterable, Set


class InvalidDirectionError(Exception):
    def __init__(self, direction: str) -> None:
        self.message = f"Invalid direction: {direction}"
        super().__init__(self.message)


@dataclass
class House:
    """When it comes to houses, all that
    matters is location, location, location!"""

    x: int
    y: int

    def __hash__(self) -> int:
        return hash((self.x, self.y))


def houses_visited(directions: Iterable[str]) -> Set[House]:
    """Santa visits houses starting at (0, 0) based on directions. He
    can either go north ("^"), south ("v"), east (">"), or west ("<").
    He will refuse to go in any other direction, and he willraise an
    exception if he is asked to do so!"""

    current: House = House(x=0, y=0)
    visited: set[House] = {current}

    for direction in directions:
        match direction:
            case "^":
                current = House(current.x, current.y + 1)
            case "v":
                current = House(current.x, current.y - 1)
            case ">":
                current = House(current.x + 1, current.y)
            case "<":
                current = House(current.x - 1, current.y)
            case _:
                raise InvalidDirectionError(direction)

        visited.add(current)

    return visited


class TestCode(unittest.TestCase):
    def test_house_equality(self):
        self.assertEqual(House(x=1, y=1), House(x=1, y=1))
        self.assertNotEqual(House(x=1, y=1), House(x=1, y=2))

    def test_houses_visited(self) -> None:
        self.assertEqual(len(houses_visited(directions=">")), 2)
        self.assertEqual(len(houses_visited(directions="^>v<")), 4)
        self.assertEqual(len(houses_visited(directions="^v^v^v^v^v")), 2)

    def test_houses_visited_with_invalid_direction(self) -> None:
        with self.assertRaises(InvalidDirectionError):
            houses_visited(directions="x")


class TestPuzzle(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.directions = f.read()

    def test_part_one(self) -> None:
        self.assertEqual(len(houses_visited(directions=self.directions)), 2565)

    def test_part_two(self) -> None:
        """Santa an Robo-Santa have had too much eggnog, and they share the
        work by taking turns to follow directions."""

        visited_by_santa = houses_visited(directions=self.directions[::2])
        visited_by_robo_santa = houses_visited(
            directions=self.directions[1::2]
        )

        self.assertEqual(
            len(visited_by_santa | visited_by_robo_santa),
            2639,
        )
