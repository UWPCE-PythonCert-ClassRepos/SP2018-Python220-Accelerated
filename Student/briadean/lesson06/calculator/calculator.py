#!/usr/bin/env python

"""Calculator class to select appropriate method"""

from calculator.exceptions import InsufficientOperands


class Calculator:
    """
    Class to take two numbers and operand and
    produce the appropriate method to calculate
    """
    def __init__(self, adder, subtracter, multiplier, divider):
        """Instantiates an instance of a calculator"""
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, num):
        """Enter a number into the calculator stack"""
        self.stack.insert(0, num)

    def _do_calc(self, operator):
        """Function to call the appropriate method and result"""
        try:
            result = operator.calc(self.stack[1], self.stack[0])
            self.stack = [result]
            return result
        except IndexError:
            raise InsufficientOperands

    def add(self):
        """Addition method"""
        return self._do_calc(self.adder)

    def subtract(self):
        """Subtraction method"""
        return self._do_calc(self.subtracter)

    def multiply(self):
        """Multiplication method"""
        return self._do_calc(self.multiplier)

    def divide(self):
        """Division method"""
        return self._do_calc(self.divider)
