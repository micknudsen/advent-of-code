import unittest


class TestCode(unittest.TestCase):
    def test_deliver_presents(self) -> None:
        self.assertEqual(deliver_presents(instructions="(())"), 0)
        self.assertEqual(deliver_presents(instructions="()()"), 0)
        self.assertEqual(deliver_presents(instructions="((("), 3)
        self.assertEqual(deliver_presents(instructions="(()(()("), 3)
        self.assertEqual(deliver_presents(instructions="))((((("), 3)
        self.assertEqual(deliver_presents(instructions="())"), -1)
        self.assertEqual(deliver_presents(instructions="))("), -1)
        self.assertEqual(deliver_presents(instructions=")))"), -3)
        self.assertEqual(deliver_presents(instructions=")())())"), -3)
