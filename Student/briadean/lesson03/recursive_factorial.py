#! /usr/local/bin/python3

"""
A recursive solution for the factorial function
"""


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
