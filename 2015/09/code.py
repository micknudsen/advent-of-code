import unittest

from collections import defaultdict
from itertools import permutations
from typing import Dict, Iterable, Iterator


class Map:
    """Class representing a map of cities and all the pairwise
    distances between them stored in a symmetric matrix implemented
    as a dictionary of dictionaries."""

    def __init__(
        self,
        distances: Dict[str, Dict[str, int]],
    ) -> None:
        self._distances = distances

    @classmethod
    def init_from_strings(
        cls,
        strings: Iterable[str],
    ) -> "Map":
        """Convenient way to initializa a Map instance from a
        list of strings as given in the puzzle input."""
        distances: Dict[str, Dict[str, int]] = defaultdict(dict)
        for string in strings:
            source, _, destination, _, distance = string.split()
            distances[source][destination] = int(distance)
            distances[destination][source] = int(distance)
        return cls(
            distances=distances,
        )

    def distance(
        self,
        source: str,
        destination: str,
    ) -> int:
        """Returns the distance between two cities."""
        return self._distances[source][destination]

    def route_lengths(self) -> Iterator[int]:
        """Iterates through all possible routes and yileds their lengths."""
        for route in permutations(self._distances.keys()):
            yield (
                sum(
                    self.distance(source, destination)
                    for source, destination in zip(route, route[1:])
                )
            )

    def shortest_route(self) -> int:
        """Returns the length of the shortest route."""
        return min(self.route_lengths())

    def longest_route(self) -> int:
        """Returns the length of the longest route."""
        return max(self.route_lengths())


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
        self.assertEqual(self.map.distance("London", "Dublin"), 464)
        self.assertEqual(self.map.distance("Dublin", "London"), 464)
        self.assertEqual(self.map.distance("London", "Belfast"), 518)
        self.assertEqual(self.map.distance("Belfast", "London"), 518)
        self.assertEqual(self.map.distance("Dublin", "Belfast"), 141)
        self.assertEqual(self.map.distance("Belfast", "Dublin"), 141)

    def test_shortest_route(self) -> None:
        self.assertEqual(self.map.shortest_route(), 605)

    def test_longest_route(self) -> None:
        self.assertEqual(self.map.longest_route(), 982)


class TestPuzzles(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.map = Map.init_from_strings(
                strings=f.read().splitlines(),
            )

    def test_part_one(self) -> None:
        self.assertEqual(self.map.shortest_route(), 117)

    def test_part_two(self) -> None:
        self.assertEqual(self.map.longest_route(), 909)
