import unittest


def paper(length: int, width: int, height: int) -> int:
    """The total square feet of wrapping paper needed for a present
    is the surface area of the box plus the area of the smallest side."""

    areas = [
        length * width,
        width * height,
        height * length,
    ]

    return 2 * sum(areas) + min(areas)


def ribbon(length: int, width: int, height: int) -> int:
    """The ribbon needed to wrap a present is the shortest distance
    around its sides plus the volume of the box."""

    perimeters = [
        2 * (length + width),
        2 * (width + height),
        2 * (height + length),
    ]

    volume = length * width * height

    return min(perimeters) + volume


class TestCode(unittest.TestCase):
    def test_paper(self) -> None:
        self.assertEqual(paper(length=2, width=3, height=4), 58)
        self.assertEqual(paper(length=1, width=1, height=10), 43)

    def test_ribbon(self) -> None:
        self.assertEqual(ribbon(length=2, width=3, height=4), 34)
        self.assertEqual(ribbon(length=1, width=1, height=10), 14)


class TestPuzzle(unittest.TestCase):
    def setUp(self) -> None:
        self.total_paper = 0
        self.total_ribbon = 0

        with open("input.txt") as f:
            for dimension in f.read().splitlines():
                length, width, height = map(int, dimension.split("x"))
                self.total_paper += paper(length=length, width=width, height=height)
                self.total_ribbon += ribbon(length=length, width=width, height=height)

    def test_part_one(self) -> None:
        self.assertEqual(self.total_paper, 1586300)

    def test_part_two(self) -> None:
        self.assertEqual(self.total_ribbon, 3737498)
