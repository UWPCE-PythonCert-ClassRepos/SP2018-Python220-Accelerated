"""
Module for converting roman numerals to integers
"""


class RomanToInt(object):
    """
    Class to create the roman to integer calculator
    """
    @staticmethod
    def value_of(roman_numeral):
        """
        Method defining conversion functions for each numeral
        """
        if roman_numeral == 'I':
            result = 1
        elif roman_numeral == 'V':
            result = 5
        elif roman_numeral == 'X':
            result = 10
        elif roman_numeral == 'L':
            result = 50
        elif roman_numeral == 'C':
            result = 100
        elif roman_numeral == 'D':
            result = 500
        elif roman_numeral == 'M':
            result = 1000
        else:
            raise ValueError(
                "Provided character must be one of: I V X L C D M.")
        return result

    @classmethod
    def convert(cls, roman_numerals):
        """
        Method that calculates the integer after converting to values
        """
        result = 0
        for i, roman_numeral in enumerate(roman_numerals):
            if ((i + 1) < len(roman_numerals)) and (
                    cls.value_of(roman_numeral) <
                    cls.value_of(roman_numerals[i + 1])):
                result -= cls.value_of(roman_numeral)
            else:
                result += cls.value_of(roman_numeral)

        return result
