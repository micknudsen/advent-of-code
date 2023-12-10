import json
import unittest


def total(document: str) -> int:
    data = json.loads(document)
    result = 0
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        for entry in data:
            result += total(json.dumps(entry))
    elif isinstance(data, dict):
        for key in data:
            result += total(json.dumps(data[key]))
    return result


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
