import unittest

from roman_numerals.roman_to_int import RomanToInt


class TestRomanToInteger(unittest.TestCase):

    def test_single_x(self):
        self.assertEqual(RomanToInt.convert('I'), 1)
        self.assertEqual(RomanToInt.convert('V'), 5)
        self.assertEqual(RomanToInt.convert('X'), 10)
        self.assertEqual(RomanToInt.convert('L'), 50)
        self.assertEqual(RomanToInt.convert('C'), 100)
        self.assertEqual(RomanToInt.convert('D'), 500)
        self.assertEqual(RomanToInt.convert('M'), 1000)


    def test_composite_x(self):
        self.assertEqual(RomanToInt.convert('LX'), 60)
        self.assertEqual(RomanToInt.convert('LXV'), 65)
        self.assertEqual(RomanToInt.convert('MMMD'), 3500)
        self.assertEqual(RomanToInt.convert('IV'), 4)
        self.assertEqual(RomanToInt.convert('MMIV'), 2004)
        self.assertEqual(RomanToInt.convert('XC'), 90)
        self.assertEqual(RomanToInt.convert('CLX'), 160)

    def test_valid_x(self):
        self.assertRaises(ValueError, RomanToInt.value_of('w'))
