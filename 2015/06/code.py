import unittest

from dataclasses import dataclass
from typing import Callable


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
        self.intensities = [
            [0 for _ in range(self.size)] for _ in range(self.size)
        ]

    def modify(self, action: str, x1: int, y1: int, x2: int, y2: int) -> None:
        match action:
            case "turn on":
                rule = self.turn_on_rule
            case "turn off":
                rule = self.turn_off_rule
            case "toggle":
                rule = self.toggle_rule
            case _:
                raise InvalidActionError(action=action)

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.intensities[x][y] = rule(self.intensities[x][y])

    def total_intensity(self) -> int:
        return sum(sum(row) for row in self.intensities)


class TestCode(unittest.TestCase):
    def test_grid(self) -> None:

        grid = Grid(
            size=1000,
            turn_on_rule=lambda x: 1,
            turn_off_rule=lambda x: 0,
            toggle_rule=lambda x: 1 - x,
        )

        # The grid starts out with no lights on
        self.assertEqual(grid.total_intensity(), 0)

        # Turn on all lights
        grid.modify(action="turn on", x1=0, y1=0, x2=999, y2=999)
        self.assertEqual(grid.total_intensity(), 1_000_000)

        # Toggle first line of lights
        grid.modify(action="toggle", x1=0, y1=0, x2=999, y2=0)
        self.assertEqual(grid.total_intensity(), 999_000)

        # Turn off middle four lights
        grid.modify(action="turn off", x1=499, y1=499, x2=500, y2=500)
        self.assertEqual(grid.total_intensity(), 998_996)
