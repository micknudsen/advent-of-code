import unittest


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
