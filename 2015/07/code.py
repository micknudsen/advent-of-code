import functools
import unittest
import re

from typing import Iterable


class ComputeError(Exception):
    def __init__(self, wire: str) -> None:
        self.message = f"Unable to compute wire: {wire}"
        super().__init__(self.message)


class Circuit:
    def __init__(self, instructions: Iterable[str]) -> None:
        self.connections: dict[str, str] = dict(
            map(lambda x: x.split(" -> ")[::-1], instructions)
        )

    @functools.cache
    def compute(self, wire: str) -> int:

        # Wire already has a number
        if wire.isdigit():
            return int(wire)

        # Signal to wire is a number
        if self.connections[wire].isdigit():
            return int(self.connections[wire])

        # Signal to wire is another wire
        if self.connections[wire] in self.connections:
            return self.compute(self.connections[wire])

        # Signal to wire is a NOT gate
        if parts := re.match(
            r"NOT (?P<value>[a-z]+|[0-9]+)", self.connections[wire]
        ):
            value = self.compute(parts.group("value"))
            return ~value + 2**16

        # Signal to wire is a binary gate
        if parts := re.match(
            r"(?P<left>[a-z]+|[0-9]+) "
            r"(?P<gate>AND|OR|LSHIFT|RSHIFT) "
            r"(?P<right>[a-z]+|[0-9]+$)",
            self.connections[wire],
        ):
            left = self.compute(parts.group("left"))
            right = self.compute(parts.group("right"))
            match parts.group("gate"):
                case "AND":
                    return left & right
                case "OR":
                    return left | right
                case "LSHIFT":
                    return left << right
                case "RSHIFT":
                    return left >> right

        raise ComputeError(wire)


class TestCode(unittest.TestCase):
    def setUp(self) -> None:
        self.circuit = Circuit(
            instructions=[
                "123 -> x",
                "456 -> y",
                "x AND y -> d",
                "x OR y -> e",
                "x LSHIFT 2 -> f",
                "y RSHIFT 2 -> g",
                "NOT x -> h",
                "NOT y -> i",
            ]
        )

    def test_compute(self) -> None:
        self.assertEqual(self.circuit.compute(wire="d"), 72)
        self.assertEqual(self.circuit.compute(wire="e"), 507)
        self.assertEqual(self.circuit.compute(wire="f"), 492)
        self.assertEqual(self.circuit.compute(wire="g"), 114)
        self.assertEqual(self.circuit.compute(wire="h"), 65412)
        self.assertEqual(self.circuit.compute(wire="i"), 65079)
        self.assertEqual(self.circuit.compute(wire="x"), 123)
        self.assertEqual(self.circuit.compute(wire="y"), 456)

    def test_compute_error(self) -> None:
        self.circuit.connections["z"] = "7 XOR 9"
        with self.assertRaises(ComputeError):
            self.circuit.compute(wire="z")


class TestPuzzle(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.circuit = Circuit(instructions=f.read().splitlines())

    def test_part_one(self) -> None:
        self.assertEqual(self.circuit.compute(wire="a"), 16076)

    def test_part_two(self) -> None:
        self.circuit.connections["b"] = "16076"
        self.assertEqual(self.circuit.compute(wire="a"), 2797)
