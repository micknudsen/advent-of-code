import json
import unittest


def total(document: str) -> int:
    match data := json.loads(document):
        case int():
            return data
        case list():
            return sum(total(json.dumps(entry)) for entry in data)
        case dict():
            return sum(total(json.dumps(data[key])) for key in data)
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


class TestPuzzles(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.document = f.read().splitlines()[0]

    def test_part_one(self) -> None:
        self.assertEqual(total(self.document), 119433)
