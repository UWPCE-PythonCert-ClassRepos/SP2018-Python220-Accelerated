'''
unit tests for the calculator program
to run from command line:
'python -m unittest test'
'''
from unittest import TestCase
from unittest.mock import MagicMock

from calculator.adder import Adder
from calculator.subtracter import Subtracter
from calculator.multiplier import Multiplier
from calculator.divider import Divider
from calculator.calculator import Calculator
from calculator.exceptions import InsufficientOperands


class AdderTests(TestCase):
    def test_adding(self):
        adder = Adder()
        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i + j, adder.calc(i, j))


class SubtracterTests(TestCase):
    def test_subtracting(self):
        subtracter = Subtracter()
        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i - j, subtracter.calc(i, j))


class CalculatorTests(TestCase):
    # setup is run each time a test method is run - BEFORE that test method
    # is run
    def setUp(self):
        self.adder = Adder()
        self.subtracter = Subtracter()
        self.multiplier = Multiplier()
        self.divider = Divider()
        self.calculator = Calculator(self.adder, self.subtracter,
                                     self.multiplier, self.divider)

    def test_insufficient_operands(self):
        self.calculator.enter_number(0)
        with self.assertRaises(InsufficientOperands):
            self.calculator.add()

    def test_adder_call(self):
        # use Mock to tell python to always return '0' when the adder method
        # is called
        # this test is not testing the adder function, so we don't care what
        # value is returned
        # using a mock value focuses the testing on the calculator class which
        # is the unit being tested here
        self.adder.calc = MagicMock(return_value=0)

        self.calculator.enter_number(1)
        self.calculator.enter_number(2)
        self.calculator.add()

        self.adder.calc.assert_called_with(1, 2)

    def test_subtracter_call(self):
        self.subtracter.calc = MagicMock(return_value=0)

        self.calculator.enter_number(1)
        self.calculator.enter_number(2)
        self.calculator.subtract()

        self.subtracter.calc.assert_called_with(1, 2)


class ModuleTests(TestCase):
    def test_module(self):
        calculator = Calculator(Adder(), Subtracter(), Multiplier(), Divider())
        calculator.enter_number(5)
        calculator.enter_number(2)
        calculator.multiply()
        calculator.enter_number(46)
        calculator.add()
        calculator.enter_number(8)
        calculator.divide()
        calculator.enter_number(1)
        result = calculator.subtract()
        self.assertEqual(6, result)


class MultiplierTests(TestCase):
    def test_multiplying(self):
        multiplier = Multiplier()
        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i * j, multiplier.calc(i, j))


class DividerTests(TestCase):
    def test_dividing(self):
        divider = Divider()
        for i in range(-10, 10):
            for j in range(-10, 10):
                if j == 0:
                    break
                self.assertEqual(i / j, divider.calc(i, j))
