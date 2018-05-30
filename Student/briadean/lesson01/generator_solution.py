#!/usr/bin/env python3

"""Exercise writing standard generators"""

# Sum of integers
def intsum():
    i = 0
    current_val = 0
    while True:
        yield current_val
        i += 1
        current_val += i

""" There is a test for intsum2, however there is no direction as to how you would like us to differentiate from intsum. """
intsum2 = intsum

# Doubler
def doubler():
    current_val = 1
    while True:
        yield current_val
        current_val *= 2


# Fibonacci sequence
def fib():
    a = 1
    b = 1
    while True:
        yield a
        a, b = b, a + b


# Prime numbers
def prime(n):
    i = 2
    while i < n:
        prime = True
        for a in range(2, i):
            if i % a == 0:
                prime = False
                break
        if prime:
            yield i
