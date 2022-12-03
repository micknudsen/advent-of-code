import unittest


class TestCode(unittest.TestCase):
    def test_mine_coin(self) -> None:
        self.assertEqual(mine_coin("abcdef"), 609043)
        self.assertEqual(mine_coin("pqrstuv"), 1048970)
