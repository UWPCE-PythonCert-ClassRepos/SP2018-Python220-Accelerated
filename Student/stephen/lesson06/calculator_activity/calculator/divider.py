"""
This module provides the division operation
"""


class Divider(object):
    """
    Class for division
    """
    @staticmethod
    def calc(operand_1, operand_2):
        """
        This method defines the division operation
        """
        try:
            operand_1 / operand_2
        except ZeroDivisionError:
            raise
        return operand_1 / operand_2
