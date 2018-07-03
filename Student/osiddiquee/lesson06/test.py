import unittest

from roman_to_int import RomanToInt


class TestRomanToInteger(unittest.TestCase):

    def test_single_x(self):
        self.assertEqual(RomanToInt.convert('X'), 10)

    def test_single_i(self):
        self.assertEqual(RomanToInt.convert('I'), 1)

    def test_single_v(self):
        self.assertEqual(RomanToInt.convert('V'), 5)

    def test_single_l(self):
        self.assertEqual(RomanToInt.convert('L'), 50)

    def test_single_c(self):
        self.assertEqual(RomanToInt.convert('C'), 100)

    def test_single_d(self):
        self.assertEqual(RomanToInt.convert('D'), 500)

    def test_single_m(self):
        self.assertEqual(RomanToInt.convert('M'), 1000)
