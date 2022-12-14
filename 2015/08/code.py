import unittest


class TestCode(unittest.TestCase):
    def test_representation_size(self) -> None:
        self.assertEqual(representation_size(r'""'), 0)
        self.assertEqual(representation_size(r'"abc"'), 3)
        self.assertEqual(representation_size(r'"aaa\"aaa"'), 7)
        self.assertEqual(representation_size(r'"\x27"'), 1)

    def test_memory_size(self) -> None:
        self.assertEqual(memory_size(r'""'), 2)
        self.assertEqual(memory_size(r'"abc"'), 5)
        self.assertEqual(memory_size(r'"aaa\"aaa"'), 10)
        self.assertEqual(memory_size(r'"\x27"'), 6)
