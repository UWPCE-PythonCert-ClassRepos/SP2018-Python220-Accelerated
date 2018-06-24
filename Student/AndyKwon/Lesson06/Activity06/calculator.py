# from exceptions import InsufficientOperands

class Calculator(object):
    def __init__(self, adder, subtracter, multiplier, divider):
        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        self.stack.insert(0, number)

    """
    def add(self):
        result = self.adder.calc(self.stack[0], self.stack[1])

    def subtracter(self):
        result = self.subtracter.calc(self.stack[0], self.stack[1])

    def multiplier(self):
        result = self.multiplier.calc(self.stack[0], self.stack[1])

    def divider(self):
        result = self.divider.calc(self.stack[0], self.stack[1])
    """
    # the below is the the above, only using an operator. not sure which is necessarily cleaner.

    def _do_calc(self, operator):
        result = operator.calc(self.stack[0], self.stack[1])
        
        # try:
        #     result = operator.calc(self.stack[0], self.stack[1])
        # except IndexError: 
        #     raise InsufficientOperands

        self.stack = [result]
        return result
    
    def add(self):
        return self._do_calc(self.adder)
    
    def subtract(self):
        return self._do_calc(self.subtracter)

    def multiply(self):
        return self._do_calc(self.multiplier)

    def divide(self):
        return self._do_calc(self.divider)
