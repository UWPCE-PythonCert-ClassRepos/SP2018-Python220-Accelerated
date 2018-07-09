#!/usr/bin/env python
'''This script converts Roman numerals to numbers'''


class RomanToInt(object):
    '''This module maps roman numerals to numbers'''

    @staticmethod
    def value_of(num):
        '''This method takes in roman numerals and returns number'''
        roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
        if num in roman_num:
            return roman_num[num]
        else:
            raise ValueError('''Provided character must be one of:
                            I V X L C D M.''')

    @classmethod
    def convert(cls, val):
        '''This method calculates total number of
         roman numerals based on order'''
        result = 0
        for i, num in enumerate(val):
            if ((i + 1) < len(val) and
                    cls.value_of(num) < cls.value_of(val[i + 1])):
                result -= cls.value_of(num)
            else:
                result += cls.value_of(num)

        return result
