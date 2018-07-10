#!/usr/bin/env python

"""Unit tests for calculator"""
from unittest import TestCase
from unittest.mock import MagicMock

from calculator.adder import Adder
from calculator.subtracter import Subtracter
from calculator.multiplier import Multiplier
from calculator.divider import Divider
from calculator.calculator import Calculator
from calculator.exceptions import InsufficientOperands


class AdderTests(TestCase):
    """Addition class test"""
    def test_adding(self):
        """Addition method test"""
        adder = Adder()
        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i + j, adder.calc(i, j))


class SubtracterTests(TestCase):
    """Subtraction class test"""
    def test_subtracting(self):
        """Subtraction method test"""
        subtracter = Subtracter()
        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i - j, subtracter.calc(i, j))


class MultiplierTests(TestCase):
    """Multiplication class test"""
    def test_multiplying(self):
        """Division method test"""
        multiplier = Multiplier()
        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i * j, multiplier.calc(i, j))


class DividerTests(TestCase):
    """Division class test"""
    def test_dividing(self):
        """Division method test"""
        divider = Divider()
        for i in range(-10, 10):
            for j in range(-10, 10):
                if j == 0:
                    break
                self.assertEqual(i / j, divider.calc(i, j))


class CalculatorTests(TestCase):
    """Calculator module test"""
    def setUp(self):
        """Set up runs prior to every unit test run"""
        self.adder = Adder()
        self.subtracter = Subtracter()
        self.multiplier = Multiplier()
        self.divider = Divider()
        self.calculator = Calculator(self.adder, self.subtracter,
                                     self.multiplier, self.divider)

    def test_insufficient_operands(self):
        """Tests for appropriate number of operands"""
        self.calculator.enter_number(0)
        with self.assertRaises(InsufficientOperands):
            self.calculator.add()

    def test_adder_call(self):
        """Test whether adder uses provided values"""
        self.adder.calc = MagicMock(return_value=0)

        self.calculator.enter_number(1)
        self.calculator.enter_number(2)
        self.calculator.add()

        self.adder.calc.assert_called_with(1, 2)

    def test_subtracter_call(self):
        """Test whether subtractor uses provided values"""
        self.subtracter.calc = MagicMock(return_value=0)

        self.calculator.enter_number(1)
        self.calculator.enter_number(2)
        self.calculator.subtract()

        self.subtracter.calc.assert_called_with(1, 2)


class ModuleTests(TestCase):
    """Calculator program test"""
    def test_module(self):
        """Test to ensure entire program operates as expected in sync"""
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
