import json
import unittest


def sum_numbers(document: str) -> int:
    data = json.loads(document)
    result = 0
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        for entry in data:
            result += sum_numbers(json.dumps(entry))
    elif isinstance(data, dict):
        for key in data:
            result += sum_numbers(json.dumps(data[key]))
    return result


class TestCode(unittest.TestCase):
    def test_sum_numbers(self) -> None:
        self.assertEqual(sum_numbers("[1,2,3]"), 6)
        self.assertEqual(sum_numbers('{"a":2,"b":4}'), 6)
        self.assertEqual(sum_numbers("[[[3]]]"), 3)
        self.assertEqual(sum_numbers('{"a":{"b":4},"c":-1}'), 3)
        self.assertEqual(sum_numbers('{"a":[-1,1]}'), 0)
        self.assertEqual(sum_numbers('[-1,{"a":1}]'), 0)
        self.assertEqual(sum_numbers("[]"), 0)
        self.assertEqual(sum_numbers("{}"), 0)

    def test_sum_numbers_ignore_red(self) -> None:
        self.assertEqual(sum_numbers("[1,2,3]", ignore_red=True), 6)
        self.assertEqual(sum_numbers('[1,{"c":"red","b":2},3]', ignore_red=True), 4)
        self.assertEqual(
            sum_numbers('{"d":"red","e":[1,2,3,4],"f":5}', ignore_red=True), 0
        )
        self.assertEqual(sum_numbers("[1,'red',5]", ignore_red=True), 6)


class TestPuzzles(unittest.TestCase):
    def setUp(self) -> None:
        with open("input.txt") as f:
            self.document = f.read().splitlines()[0]

    def test_part_one(self) -> None:
        self.assertEqual(sum_numbers(self.document), 119433)
