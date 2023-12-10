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
