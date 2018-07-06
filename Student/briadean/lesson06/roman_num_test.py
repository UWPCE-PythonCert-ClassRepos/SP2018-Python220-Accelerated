import unittest
from lesson06.roman_numerals import RomanToInt


class TestRomanToInt(unittest.TestCase):

    def test_input_valid(self):

        self.inputval = ('I', 'V', 'X', 'L', 'C', 'D', 'M')

        for iv in self.inputval:
            assert RomanToInt.value_of(iv) is not ValueError('''Provided character must be one of: I V X L C D M.''')

    def test_single_i(self):
        self.assertEqual(RomanToInt.convert('I'), 1)

    def test_single_v(self):
        self.assertEqual(RomanToInt.convert('V'), 5)

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
