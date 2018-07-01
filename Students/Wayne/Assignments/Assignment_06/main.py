import sys

from roman_numerals.roman_to_int import RomanToInt


if __name__ == "__main__":
    s = sys.argv[1]

    print("The Roman numerals {} are {} in decimal.".format(s, RomanToInt.convert(s)))
