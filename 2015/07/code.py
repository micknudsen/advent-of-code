import unittest
import re

from typing import Iterable


class Circuit:
    def __init__(self, instructions: Iterable[str]) -> None:
        self.connections: dict[str, str] = dict(
            map(lambda x: x.split(" -> ")[::-1], instructions)
        )

    def compute(self, wire: str) -> int:

        if wire.isdigit():
            return int(wire)

        if self.connections[wire].isdigit():
            return int(self.connections[wire])

        if parts := re.match(
            r"NOT (?P<value>[a-z]+|[0-9]+)", self.connections[wire]
        ):
            value = self.compute(parts.group("value"))
            return ~value + 2**16

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

        raise Exception(wire)


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
