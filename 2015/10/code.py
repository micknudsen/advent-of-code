import unittest


class TestCode(unittest.TestCase):

    def test_say(self) -> None:
        self.assertEqual(say(number="1"), "11",)
        self.assertEqual(say(number="11"), "21",)
        self.assertEqual(say(number="21"), "1211",)
        self.assertEqual(say(number="1211"), "111221",)
        self.assertEqual(say(number="111221"), "312211",)
