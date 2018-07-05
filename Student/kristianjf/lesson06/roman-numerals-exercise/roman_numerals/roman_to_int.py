##!/usr/bin/env python3
'''Convert Roman Numerals to Integers'''


class RomanToInt(object):
    '''Class to manage roman numeral to integer conversion'''
    @staticmethod
    def value_of(roman_num):
        '''Equate roman numeral to integer'''
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                      'D': 500, 'M': 1000}
        if roman_num in roman_dict:
            return roman_dict.get(roman_num)
        else:
            raise ValueError(
                "Provided character must be one of: I V X L C D M.")

    @classmethod
    def convert(cls, roman_num_in):
        '''Logic to convert roman numeral to integer'''
        result = 0
        for i, roman_num in enumerate(roman_num_in):
            if (i + 1) < len(roman_num_in) and cls.value_of(roman_num) < \
               cls.value_of(roman_num_in[i + 1]):
                result -= cls.value_of(roman_num)
            else:
                result += cls.value_of(roman_num)

        return result
