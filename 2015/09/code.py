import unittest


class TestCode(unittest.TestCase):
    def setUp(self) -> None:
        self.locations: dict[str, Location] = locations_from_strings(
            [
                "London to Dublin = 464",
                "London to Belfast = 518",
                "Dublin to Belfast = 141",
            ]
        )

    def test_distance(self) -> None:
        self.assertEqual(
            self.locations["London"].distance("Dublin"),
            464,
        )
        self.assertEqual(
            self.locations["Dublin"].distance("London"),
            464,
        )
        self.assertEqual(
            self.locations["London"].distance("Belfast"),
            518,
        )
        self.assertEqual(
            self.locations["Belfast"].distance("London"),
            518,
        )
        self.assertEqual(
            self.locations["Dublin"].distance("Belfast"),
            141,
        )
        self.assertEqual(
            self.locations["Belfast"].distance_to("Dublin"),
            141,
        )

    def test_shortest_route(self) -> None:
        self.assertEqual(
            shortest_route(self.locations),
            605,
        )
