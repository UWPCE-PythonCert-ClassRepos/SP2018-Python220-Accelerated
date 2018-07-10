'''
main calculator program
'''

from .exceptions import InsufficientOperands


class Calculator():
    '''
    demonstrating architecture of:
    Dependency Inversion or Dependency Injection
    '''

    def __init__(self, adder, subtracter, multiplier, divider):
        '''
        instantiates an instance of a calculator
        '''
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        '''
        enter a number into the calculator stack
        '''
        self.stack.insert(0, number)

    def _do_calc(self, operator):
        '''
        function that will call the appropriate class and to retrieve the
        result
        '''
        try:
            result = operator.calc(self.stack[1], self.stack[0])
            self.stack = [result]
            return result
        except IndexError:
            raise InsufficientOperands

    def add(self):
        '''
        add method
        '''
        return self._do_calc(self.adder)

    def subtract(self):
        '''
        subtraction method
        '''
        return self._do_calc(self.subtracter)

    def multiply(self):
        '''
        multiplication method
        '''
        return self._do_calc(self.multiplier)

    def divide(self):
        '''
        division method
        '''
        return self._do_calc(self.divider)
