import unittest

from roman_to_int import RomanToInt


class TestRomanToInteger(unittest.TestCase):

    # singles
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


    # composite examples
    def test_composite_LX(self):
        self.assertEqual(RomanToInt.convert('LX'), 60)

    def test_composite_LXV(self):
        self.assertEqual(RomanToInt.convert('LXV'), 65)

    def test_composite_MMMD(self):
        self.assertEqual(RomanToInt.convert('MMMD'), 3500)



    # inputs
    def test_valid(self):
        self.value = ('I', 'V', 'X', 'L', 'C', 'D', 'M')

        for iv in self.value:
            assert RomanToInt.value_of(iv) is not ValueError('''Provided character must be one of: I V X L C D M.''')


    """

    All tests passed:
    
    Tammys-MBP:roman_numerals tammydo$ python -m unittest test_roman_to_int.py 
    ...........
    ----------------------------------------------------------------------
    Ran 11 tests in 0.003s

    OK
    Tammys-MBP:roman_numerals tammydo$ 

    """
