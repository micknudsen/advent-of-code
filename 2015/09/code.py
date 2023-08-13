import unittest

from collections import defaultdict
from itertools import permutations
from typing import Dict


class Map:
    def __init__(self, distances: Dict[str, Dict[str, int]]) -> None:
        self.distances = distances

    @classmethod
    def init_from_strings(
        cls,
        strings: str,
    ) -> "Map":
        distances: Dict[str, Dict[str, int]] = defaultdict(dict)
        for string in strings:
            source, _, destination, _, distance = string.split()
            distances[source][destination] = int(distance)
            distances[destination][source] = int(distance)
        return cls(distances)

    def distance(
        self,
        source: str,
        destination: str,
    ) -> int:
        return self.distances[source][destination]

    def shortest_route(self) -> int:
        return min(
            sum(
                self.distance(source, destination)
                for source, destination in zip(route, route[1:])
            )
            for route in permutations(self.distances.keys())
        )

    def longest_route(self) -> int:
        return max(
            sum(
                self.distance(source, destination)
                for source, destination in zip(route, route[1:])
            )
            for route in permutations(self.distances.keys())
        )


class TestCode(unittest.TestCase):
    def setUp(self) -> None:
        self.map = Map.init_from_strings(
            [
                "London to Dublin = 464",
                "London to Belfast = 518",
                "Dublin to Belfast = 141",
            ]
        )

    def test_distance(self) -> None:
        self.assertEqual(
            self.map.distance("London", "Dublin"),
            464,
        )
        self.assertEqual(
            self.map.distance("Dublin", "London"),
            464,
        )
        self.assertEqual(
            self.map.distance("London", "Belfast"),
            518,
        )
        self.assertEqual(
            self.map.distance("Belfast", "London"),
            518,
        )
        self.assertEqual(
            self.map.distance("Dublin", "Belfast"),
            141,
        )
        self.assertEqual(
            self.map.distance("Belfast", "Dublin"),
            141,
        )

    def test_shortest_route(self) -> None:
        self.assertEqual(
            self.map.shortest_route(),
            605,
        )

    def test_longest_route(self) -> None:
        self.assertEqual(
            self.map.longest_route(),
            982,
        )


class TestPuzzles(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.map = Map.init_from_strings(
                strings=f.read().splitlines(),
            )

    def test_part_one(self) -> None:
        self.assertEqual(
            self.map.shortest_route(),
            117,
        )
