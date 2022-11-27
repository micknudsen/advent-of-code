import unittest


def paper_needed(lenght: int, width: int, height: int) -> int:
    """To wrap a box, the elves need to cover the surface area, and
    for some reason they also need a little extra paper with an area
    equals to the area of the smallest side of the box."""

    areas = [lenght * width, width * height, height * lenght]
    return 2 * sum(areas) + min(areas)


class TestCode(unittest.TestCase):
    def test_paper_needed(self) -> None:
        self.assertEqual(paper_needed(lenght=2, width=3, height=4), 58)
        self.assertEqual(paper_needed(lenght=1, width=1, height=10), 43)
