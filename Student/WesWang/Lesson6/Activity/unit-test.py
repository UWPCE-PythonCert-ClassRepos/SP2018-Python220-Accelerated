from unittest import TestCase
from unittest.mock import MagicMock

from adder import Adder
from subtracter import Subtracter
from multiplier import Multiplier
from divider import Divider
from calculator import Calculator

class AdderTest(TestCase):

    def test_adding(self):
        add = Adder()

        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i + j, adder.calc(i, j))


class SubtracterTest(TestCase):

    def test_subtracting(self):
        subtract = Subtracter()

        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i + j, subtracter.calc(i, j))


class AdderTest(TestCase):

    def test_adding(self):
        add = Adder()

        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i + j, add.calc(i, j))


class SubtracterTest(TestCase):

    def test_subtracting(self):
        subtract = Subtracter()

        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i - j, subtract.calc(i, j))


class MultiplierTest(TestCase):

    def test_multiplying(self):
        multiply = Multiplier()

        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i * j, multiply.calc(i, j))


class DividerTest(TestCase):

    def test_dividing(self):
        divide = Divider()

        for i in range(-10, 10):
            for j in range(-10, 10):
                if j == 0:
                    pass
                else:
                    self.assertEqual(i / j, divide.calc(i, j))


class CalculatorTests(TestCase):

    def setUp(self):
        self.adder = Adder()
        self.subtracter = Subtracter()
        self.multiplier = Multiplier()
        self.divider = Divider()

        self.calculator = Calculator(self.adder, self.subtracter, self.multiplier, self.divider)

    def test_insufficient_operands(self):
        self.calculator.enter_number(0)

        with self.assertRaises(IndexError):
            self.calculator.add()

    def test_adder_call(self):
        self.adder.calc = MagicMock(return_value=0)

        self.calculator.enter_number(1)
        self.calculator.enter_number(2)
        self.calculator.add()

        self.adder.calc.assert_called_with(1, 2)

    def test_subtrater_call(self):
        self.subtracter.calc = MagicMock(return_value=0)

        self.calculator.enter_number(1)
        self.calculator.enter_number(2)
        self.calculator.subtract()

        self.subtracter.calc.assert_called_with(1, 2)

    def test_multiplier_call(self):
        self.multiplier.calc = MagicMock(return_value=0)

        self.calculator.enter_number(3)
        self.calculator.enter_number(2)
        self.calculator.multiply()

        self.multiplier.calc.assert_called_with(3, 2)

    def test_divider_call(self):
        self.divider.calc = MagicMock(return_value=0)

        self.calculator.enter_number(4)
        self.calculator.enter_number(2)
        self.calculator.divide()

        self.divider.calc.assert_called_with(4, 2)