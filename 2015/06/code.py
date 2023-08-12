import unittest
import re

from dataclasses import dataclass
from typing import Callable, List, Tuple


class InvalidActionError(Exception):
    def __init__(self, action: str) -> None:
        self.message = f"Invalid action: {action}"
        super().__init__(self.message)


@dataclass
class Grid:
    size: int
    turn_on_rule: Callable[[int], int]
    turn_off_rule: Callable[[int], int]
    toggle_rule: Callable[[int], int]

    def __post_init__(self) -> None:
        self.intensities = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def switch(self, action: str, i1: int, j1: int, i2: int, j2: int) -> None:
        match action:
            case "turn on":
                rule = self.turn_on_rule
            case "turn off":
                rule = self.turn_off_rule
            case "toggle":
                rule = self.toggle_rule
            case _:
                raise InvalidActionError(action=action)

        for i in range(i1, i2 + 1):
            for j in range(j1, j2 + 1):
                self.intensities[i][j] = rule(self.intensities[i][j])

    def total_intensity(self) -> int:
        return sum(sum(row) for row in self.intensities)


class TestCode(unittest.TestCase):
    def test_first_grid(self) -> None:
        grid = Grid(
            size=1000,
            turn_on_rule=lambda x: 1,
            turn_off_rule=lambda x: 0,
            toggle_rule=lambda x: 1 - x,
        )

        # The grid starts out with no lights on
        self.assertEqual(grid.total_intensity(), 0)

        # Turn on all lights
        grid.switch(action="turn on", i1=0, j1=0, i2=999, j2=999)
        self.assertEqual(grid.total_intensity(), 1_000_000)

        # Toggle first line of lights
        grid.switch(action="toggle", i1=0, j1=0, i2=999, j2=0)
        self.assertEqual(grid.total_intensity(), 999_000)

        # Turn off middle four lights
        grid.switch(action="turn off", i1=499, j1=499, i2=500, j2=500)
        self.assertEqual(grid.total_intensity(), 998_996)

        # Invalid action raises an exception
        with self.assertRaises(InvalidActionError):
            grid.switch(action="change color", i1=0, j1=0, i2=0, j2=0)

    def test_second_grid(self) -> None:
        grid = Grid(
            size=1000,
            turn_on_rule=lambda x: x + 1,
            turn_off_rule=lambda x: max(x - 1, 0),
            toggle_rule=lambda x: x + 2,
        )

        # The grid starts out with no lights on
        self.assertEqual(grid.total_intensity(), 0)

        # Turn on one light
        grid.switch(action="turn on", i1=0, j1=0, i2=0, j2=0)
        self.assertEqual(grid.total_intensity(), 1)

        # Toggle all ligths
        grid.switch(action="toggle", i1=0, j1=0, i2=999, j2=999)
        self.assertEqual(grid.total_intensity(), 2_000_001)


class TestPuzzle(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.instructions: List[Tuple[str, int, int, int, int]] = []
            for line in f.read().splitlines():
                if instruction := re.match(
                    "(?P<action>[a-z ]+)"
                    "(?P<i1>[0-9]+),(?P<j1>[0-9]+)"
                    " through "
                    "(?P<i2>[0-9]+),(?P<j2>[0-9]+)",
                    line,
                ):
                    self.instructions.append(
                        (
                            instruction.group("action").rstrip(),
                            int(instruction.group("i1")),
                            int(instruction.group("j1")),
                            int(instruction.group("i2")),
                            int(instruction.group("j2")),
                        ),
                    )

    def test_part_one(self) -> None:
        grid = Grid(
            size=1000,
            turn_on_rule=lambda x: 1,
            turn_off_rule=lambda x: 0,
            toggle_rule=lambda x: 1 - x,
        )
        for action, i1, j1, i2, j2 in self.instructions:
            grid.switch(action=action, i1=i1, j1=j1, i2=i2, j2=j2)
        self.assertEqual(grid.total_intensity(), 377891)

    def test_part_two(self) -> None:
        grid = Grid(
            size=1000,
            turn_on_rule=lambda x: x + 1,
            turn_off_rule=lambda x: max(x - 1, 0),
            toggle_rule=lambda x: x + 2,
        )
        for action, i1, j1, i2, j2 in self.instructions:
            grid.switch(action=action, i1=i1, j1=j1, i2=i2, j2=j2)
        self.assertEqual(grid.total_intensity(), 14110788)
