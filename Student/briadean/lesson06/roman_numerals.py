#!/usr/bin/env python
"""
Script to convert roman numerals to numbers
"""


class RomanToInt(object):
    """Module maps roman numerals to numbers"""

    @staticmethod
    def value_of(roman_num):
        """Method to take a roman numeral and return a number"""
        roman_dict = {'I': 1,
                      'V': 5,
                      'X': 10,
                      'L': 50,
                      'C': 100,
                      'D': 500,
                      'M': 1000}

        if roman_num in roman_dict:
            return roman_dict.get(roman_num)
        else:
            raise ValueError("Provided character must be one of: I V X L C D M.")

    @classmethod
    def convert(cls, roman_nums):
        """Method to calculate roman numeral conversion """
        result = 0
        for i, roman_num in enumerate(roman_nums):
            if (i + 1) < len(roman_nums) and \
                    cls.value_of(roman_num) < cls.value_of(roman_nums[i + 1]):
                result -= cls.value_of(roman_num)
            else:
                result += cls.value_of(roman_num)

        return result
