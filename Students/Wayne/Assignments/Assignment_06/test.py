import unittest

from roman_numerals.roman_to_int import RomanToInt


class TestRomanToInteger(unittest.TestCase):

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

    def test_values(self):
        self.multiplevalues = (('II', 2),
                               ('III', 3),
                               ('IV', 4),
                               ('VI', 6),
                               ('VII', 7),
                               ('VIII', 8),
                               ('IX', 9),
                               ('MCMLXXXVII', 1987),
                               ('MCMXCIX', 1999),
                               ('MMCXI', 2111),
                               ('MMCCXXII', 2222),
                               ('MMCCCXXXIII', 2333),
                               ('MMCDXLIV', 2444),
                               ('MMDLV', 2555),
                               ('MMDCLXVI', 2666),
                               ('MMDCCLXXVII', 2777),
                               ('MMDCCCLXXXVIII', 2888),
                               ('MMCMXCIX', 2999),
                               ('MMMLXXXVIII', 3088),
                               ('MMMCCLXIX', 3269),
                               ('MMMCDXXVIII', 3428),
                               ('MMMDCLXXXVIII', 3688),
                               ('MMMDCCXCVIII', 3798),
                               ('MMMCMXCIX', 3999))

        for roman_numerals, integer in self.multiplevalues:
            result = RomanToInt.convert(roman_numerals)
            self.assertEqual(result, integer)

    def test_valid_value_of_input(self):

        self.inputvalues = ('I', 'V', 'X', 'L', 'C', 'D', 'M')

        for iv in self.inputvalues:
            assert RomanToInt.value_of(iv) is not ValueError(
                '''Provided character must be one of: I V X L C D M.''')

    def test_invalid_value_of_input(self):

        self.invalidinputvalues = ['i', 'v', 'x', 'v', 'c', 'd', 'm',
                                   1, 5, 10, 50, 100, 500, 1000]

        for okiv in self.invalidinputvalues:
            self.assertRaises(ValueError('''Provided character must be one of: I V X L C D M.''')) 

    def test_valid_value_of_c(self):
        self.c_values = (('I', 1),
                         ('V', 5),
                         ('X', 10),
                         ('L', 50),
                         ('C', 100),
                         ('D', 500),
                         ('M', 1000))
        for roman_numerals, integer in self.c_values:
            result = RomanToInt.value_of(roman_numerals)
            self.assertEqual(result, integer)
