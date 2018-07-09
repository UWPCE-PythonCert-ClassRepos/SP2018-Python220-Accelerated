#!/usr/bin/env python
'''This script is a calculator'''


class Calculator(object):
    '''This module contains add, subtract, multiply, divide functions'''

    def __init__(self, adder, subtracter, multiplier, divider):
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        '''This method append input number into list'''
        self.stack.append(number)

    def _do_calc(self, operator):
        '''This method calculate the two numbers in list based on input operator'''
        result = operator.calc(self.stack[0], self.stack[1])
        self.stack = [result]
        return result

    def add(self):
        '''This method insert add operator to _do_calc'''
        return self._do_calc(self.adder)

    def subtract(self):
        '''This method insert subtract operator to _do_calc'''
        return self._do_calc(self.subtracter)

    def multiply(self):
        '''This method insert multiply operator to _do_calc'''
        return self._do_calc(self.multiplier)

    def divide(self):
        '''This method insert divide operator to _do_calc'''
        return self._do_calc(self.divider)
    