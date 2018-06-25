import unittest

from roman_numerals.roman_to_int import RomanToInt


class TestRomanToInteger(unittest.TestCase):
    
    def test_single_x(self):
        self.assertEqual(RomanToInt.convert('X'), 10)

    def test_single_l(self):
        self.assertEqual(RomanToInt.convert('L'), 50)

    def test_single_c(self):
        self.assertEqual(RomanToInt.convert('C'), 100)

    def test_single_d(self):
        self.assertEqual(RomanToInt.convert('D'), 500)

    def test_single_m(self):
        self.assertEqual(RomanToInt.convert('M'), 1000)

    def test_comp_1(self):
        self.assertEqual(RomanToInt.convert('LX'), 60)
            
    def test_comp_2(self):
        self.assertEqual(RomanToInt.convert('LXV'), 65)
        
    def test_comp_3(self):
        self.assertEqual(RomanToInt.convert('MMMD'), 3500)
        
    def test_sub_1(self):
        self.assertEqual(RomanToInt.convert('IV'), 4)
        
    def test_sub_2(self):
        self.assertEqual(RomanToInt.convert('MMIV'), 2004)
        
    def test_sub_3(self):
        self.assertEqual(RomanToInt.convert('XC'), 90)

    def test_error(self):
        with self.assertRaises(ValueError):
            RomanToInt.convert('Q')

