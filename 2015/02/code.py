import unittest


def paper_needed(
    lenght: int,
    width: int,
    height: int,
) -> int:
    """To wrap a box, the elves need to cover the surface area, and
    for some reason they also need a little extra paper with an area
    equals to the area of the smallest side of the box."""

    areas = [
        lenght * width,
        width * height,
        height * lenght,
    ]
    return 2 * sum(areas) + min(areas)


def ribbon_needed(
    lenght: int,
    width: int,
    height: int,
) -> int:
    """To wrap a box, the elves need a bow made out of ribbon. The
    required lenght is the smallest perimeter of any one face. An
    additional amount of ribbon of length equal to the volume of
    the box is needed. The elves work in mysterious ways."""

    perimeters = [
        2 * (lenght + width),
        2 * (width + height),
        2 * (height + lenght),
    ]
    return min(perimeters) + lenght * width * height


class TestCode(unittest.TestCase):
    def test_paper_needed(self) -> None:
        self.assertEqual(
            paper_needed(
                lenght=2,
                width=3,
                height=4,
            ),
            58,
        )
        self.assertEqual(
            paper_needed(
                lenght=1,
                width=1,
                height=10,
            ),
            43,
        )

    def test_ribbon_needed(self) -> None:
        self.assertEqual(
            ribbon_needed(
                lenght=2,
                width=3,
                height=4,
            ),
            34,
        )
        self.assertEqual(
            ribbon_needed(
                lenght=1,
                width=1,
                height=10,
            ),
            14,
        )


class TestPuzzle(unittest.TestCase):
    def setUp(self) -> None:
        """Puzzle input is a list of box dimonsions. Calculate the total
        amount of paper and ribbon needed to wrap all the boxes."""

        self.total_paper = 0
        self.total_ribbon = 0

        with open("input.txt") as f:
            for dimension in f.read().splitlines():
                lenght, width, height = map(
                    int,
                    dimension.split("x"),
                )
                self.total_paper += paper_needed(
                    lenght=lenght, width=width, height=height
                )
                self.total_ribbon += ribbon_needed(
                    lenght=lenght, width=width, height=height
                )

    def test_part_one(self) -> None:
        self.assertEqual(
            self.total_paper,
            1586300,
        )

    def test_part_two(self) -> None:
        self.assertEqual(
            self.total_ribbon,
            3737498,
        )
