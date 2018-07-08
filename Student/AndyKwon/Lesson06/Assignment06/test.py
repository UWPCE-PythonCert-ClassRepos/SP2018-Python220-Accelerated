from unittest import TestCase
from roman_to_int import RomanToInt

class TestRomanToInteger(TestCase):
    
    def test_single_x(self):
        lst_letter = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        lst_number = [1, 5, 10, 50, 100, 500, 1000]

        for letter, number in zip(lst_letter, lst_number):
            self.assertEqual(RomanToInt.convert(letter), number)
    
    def test_double_x(self):
        self.assertEqual(RomanToInt.convert('III'), 3)
        self.assertEqual(RomanToInt.convert('IV'), 4)
        self.assertEqual(RomanToInt.convert('IX'), 9)
        self.assertEqual(RomanToInt.convert('XX'), 20)
        self.assertEqual(RomanToInt.convert('XXVII'), 27)
        self.assertEqual(RomanToInt.convert('XXX'), 30)
        self.assertEqual(RomanToInt.convert('XL'), 40)
        self.assertEqual(RomanToInt.convert('XC'), 90)












