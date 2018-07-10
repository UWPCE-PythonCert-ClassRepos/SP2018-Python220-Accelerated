"""
This module provides the Calculator class and methods
"""


from .exceptions import InsufficientOperands


class Calculator(object):
    """
    Class defining the Calculator class of arithmatic operations
    """
    def __init__(self, adder, subtracter, multiplier, divider):
        """
        Initialize the class, creating operation attributes and stack attribute
        """
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        """
        Method for getting operands and inserting into stack
        """
        self.stack.insert(0, number)

    def _do_calc(self, operator):
        """
        Return the result of the calculation, reversing order of the stack
        to reflect order of operands in calculator methods
        """
        try:
            result = operator.calc(self.stack[1], self.stack[0])
        except IndexError:
            raise InsufficientOperands

        self.stack = [result]
        return result

    def add(self):
        """
        Addition calculation
        """
        return self._do_calc(self.adder)

    def subtract(self):
        """
        Subtraction calculation
        """
        return self._do_calc(self.subtracter)

    def multiply(self):
        """
        Multiplication calculation
        """
        return self._do_calc(self.multiplier)

    def divide(self):
        """
        Division calculation
        """
        try:
            result = self._do_calc(self.divider)
        except ZeroDivisionError:
            self.stack = self.stack[1:]
            print('Cannot divide by zero. Try another number.')
            raise
        else:
            return result
