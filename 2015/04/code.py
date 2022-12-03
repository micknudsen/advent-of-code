import hashlib
import unittest


def mine_coin(key: str, hardness: int = 5) -> int:
    number = 1
    while True:
        digest = hashlib.md5(f"{key}{number}".encode()).hexdigest()
        if digest.startswith("0" * hardness):
            return number
        number += 1


class TestCode(unittest.TestCase):
    def test_mine_coin(self) -> None:
        self.assertEqual(mine_coin("abcdef"), 609043)
        self.assertEqual(mine_coin("pqrstuv"), 1048970)


class TestPuzzle(unittest.TestCase):
    def setUp(self) -> None:
        self.key = "iwrupvqb"

    def test_part_one(self) -> None:
        self.assertEqual(mine_coin(key=self.key), 346386)

    def test_part_two(self) -> None:
        self.assertEqual(mine_coin(key=self.key, hardness=6), 9958218)
