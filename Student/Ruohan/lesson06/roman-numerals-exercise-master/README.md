# Roman Numerals, Advanced Testing Exercise

Before the invention and wide-spread use of the number "zero", many cultures used different ways to represent large numbers. This exercise is based on the Roman method of representing large numbers, known as "Roman numerals."

In the Roman numeral system, certain characters represent certain numbers. The following table gives the number value of the Roman numerals that we will use in this exercise:

* I: 1
* V: 5
* X: 10
* L: 50
* C: 100
* D: 500
* M: 1000

A composite number can be produced by listing several characters, from largest-valued to smallest-valued and adding their values. For example:

* LX: 60
* LXV: 65
* MMMD: 3500

Additionally, if a smaller-valued numeral _comes before_ a larger-valued numeral, then that value is subtracted from the total value, rather than added. For example:

* IV: (5 - 1): 4
* MMIV: 1000 + 1000 + (5 - 1): 2004
* XC: (100 - 10): 90

There's a version of the Roman numeral system where _any_ smaller-valued numeral which comes before a larger-valued numeral is subtracted from the total, but we won't use that version of numerals.

This repository includes a `RomanToInt` class which can convert a Roman numeral string into an integer. The class works on Roman numeral strings with a value up to 3999. You can use this class at the command line, using the included `main.py`. For example: `python main.py IMMMM`.

## Your Goals

1. Write a comprehensive set of tests into `test.py`.
2. All of your tests should pass, using: `python -m unittest test.py`.
3. Running `coverage run --source=roman_numerals -m unittest test.py; coverage report` should give a coverage of 100%.
4. Satisfy the linter such that `pylint roman_numerals` and `flake8 roman_numerals` show no errors.

## Additional Comments

Feel free to satisfy the linter through any combination of making improvements to the files and/or creating a pylint configuration file which ignores particular errors. If you create a custom configuration file, then be sure to `git include` it in your repository.

For the purposes of this exercise, the code may include some bad style. Feel free to refactor the code if you see opportunities for improvement.
