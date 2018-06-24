from unittest import TestCase
from roman_to_int import RomanToInt

class TestRomanToInteger(TestCase):
    
    def test_single_x(self):
        lst_letter = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        lst_number = [1, 5, 10, 50, 100, 500, 1000]

        for letter, number in zip(lst_letter, lst_number):
            self.assertEqual(RomanToInt.convert(letter), number)
            print("pass")


        # self.assertEqual(RomanToInt.convert('X'), 10)
    
    def test_double_x(self):
        self.assertEqual(RomanToInt.convert('XX'), 20)












