import unittest

from roman_numerals.roman_to_int import RomanToInt


class TestRomanToInteger(unittest.TestCase):

    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    def test_roman_numerals(self):
        for roman_num, num in self.roman_dict.items():
            self.assertEqual(RomanToInt.convert(roman_num), num)

    def test_small_large(self):
        for i in range(len(self.roman_dict)-1):
            roman_tuple = sorted(self.roman_dict.items(), key=lambda x: x[1])
            two_roman = roman_tuple[i][0] + roman_tuple[i+1][0]
            two_num = (roman_tuple[i][1], roman_tuple[i+1][1])
            self.assertEqual(RomanToInt.convert(two_roman), (lambda x: x[1] - x[0])(x=two_num))

    def test_errors(self):
        with self.assertRaises(ValueError):
            RomanToInt.convert('A')
