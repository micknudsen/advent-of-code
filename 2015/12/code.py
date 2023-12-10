import json
import unittest

from typing import Optional


def total(
    document: str,
    ignore_red: Optional[bool] = False,
) -> int:
    match data := json.loads(document):
        case int():
            return data
        case list():
            return sum(
                total(
                    json.dumps(entry),
                    ignore_red=ignore_red,
                )
                for entry in data
            )
        case dict():
            if ignore_red and "red" in data.values():
                return 0
            return sum(
                total(
                    json.dumps(data[key]),
                    ignore_red=ignore_red,
                )
                for key in data
            )
        case _:
            return 0


class TestCode(unittest.TestCase):
    def test_total(self) -> None:
        self.assertEqual(total("[1,2,3]"), 6)
        self.assertEqual(total('{"a":2,"b":4}'), 6)
        self.assertEqual(total("[[[3]]]"), 3)
        self.assertEqual(total('{"a":{"b":4},"c":-1}'), 3)
        self.assertEqual(total('{"a":[-1,1]}'), 0)
        self.assertEqual(total('[-1,{"a":1}]'), 0)
        self.assertEqual(total("[]"), 0)
        self.assertEqual(total("{}"), 0)

    def test_total_ignore_red(self) -> None:
        self.assertEqual(total("[1,2,3]", ignore_red=True), 6)
        self.assertEqual(total('[1,{"c":"red","b":2},3]', ignore_red=True), 4)
        self.assertEqual(total('{"d":"red","e":[1,2,3,4],"f":5}', ignore_red=True), 0)
        self.assertEqual(total('[1,"red",5]', ignore_red=True), 6)


class TestPuzzles(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.document = f.read().splitlines()[0]

    def test_part_one(self) -> None:
        self.assertEqual(total(self.document), 119433)

    def test_part_two(self) -> None:
        self.assertEqual(total(self.document, ignore_red=True), 68466)
