import unittest


def paper_needed(length: int, width: int, height: int) -> int:

    areas = [
        length * width,
        width * height,
        height * length,
    ]

    return 2 * sum(areas) + min(areas)


def ribbon_needed(length: int, width: int, height: int) -> int:

    perimeters = [
        2 * (length + width),
        2 * (width + height),
        2 * (height + length),
    ]

    volume = length * width * height

    return min(perimeters) + volume


class TestCode(unittest.TestCase):
    def test_paper_needed(self) -> None:
        self.assertEqual(paper_needed(length=2, width=3, height=4), 58)
        self.assertEqual(paper_needed(length=1, width=1, height=10), 43)

    def test_ribbon_needed(self) -> None:
        self.assertEqual(ribbon_needed(length=2, width=3, height=4), 34)
        self.assertEqual(ribbon_needed(length=1, width=1, height=10), 14)


class TestPuzzle(unittest.TestCase):
    def setUp(self) -> None:
        self.total_paper = 0
        self.total_ribbon = 0

        with open("input.txt") as f:
            for dimension in f.read().splitlines():
                length, width, height = map(int, dimension.split("x"))
                self.total_paper += paper_needed(
                    length=length, width=width, height=height
                )
                self.total_ribbon += ribbon_needed(
                    length=length, width=width, height=height
                )

    def test_part_one(self) -> None:
        self.assertEqual(self.total_paper, 1586300)

    def test_part_two(self) -> None:
        self.assertEqual(self.total_ribbon, 3737498)
