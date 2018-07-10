"""
Module for unit testing roman numerals to integer program
"""


import unittest

from roman_numerals.roman_to_int import RomanToInt


class TestRomanToInteger(unittest.TestCase):
    
    def test_single_I(self):
        self.assertEqual(RomanToInt.convert('I'), 1)

    def test_single_V(self):
        self.assertEqual(RomanToInt.convert('V'), 5)

    def test_single_X(self):
        self.assertEqual(RomanToInt.convert('X'), 10)

    def test_single_L(self):
        self.assertEqual(RomanToInt.convert('L'), 50)

    def test_single_C(self):
        self.assertEqual(RomanToInt.convert('C'), 100)

    def test_single_D(self):
        self.assertEqual(RomanToInt.convert('D'), 500)

    def test_single_M(self):
        self.assertEqual(RomanToInt.convert('M'), 1000)

    def test_multiple_numerals(self):
        self.assertEqual(RomanToInt.convert('MMIV'), 2004)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            RomanToInt.convert('ZZZ')
