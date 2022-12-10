import unittest


class Grid:
    def __init__(self, width: int, height: int) -> None:
        self.lights = [[0 for _ in range(width)] for _ in range(height)]

    def turn_on(self, x1: int, y1: int, x2: int, y2: int) -> None:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.lights[x][y] = 1

    def turn_off(self, x1: int, y1: int, x2: int, y2: int) -> None:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.lights[x][y] = 0

    def toggle(self, x1: int, y1: int, x2: int, y2: int) -> None:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.lights[x][y] = 1 - self.lights[x][y]

    def count_lights_on(self) -> int:
        return sum(sum(row) for row in self.lights)


class TestCode(unittest.TestCase):
    def test_grid(self) -> None:

        grid = Grid(height=1000, width=1000)

        # The grid starts out with no lights on
        self.assertEqual(grid.count_lights_on(), 0)

        # Turn on all lights
        grid.turn_on(x1=0, y1=0, x2=999, y2=999)
        self.assertEqual(grid.count_lights_on(), 1_000_000)

        # Toggle first line of lights
        grid.toggle(x1=0, y1=0, x2=999, y2=0)
        self.assertEqual(grid.count_lights_on(), 999_000)

        # Turn off middle four lights
        grid.turn_off(x1=499, y1=499, x2=500, y2=500)
        self.assertEqual(grid.count_lights_on(), 998_996)
