#!/usr/bin/env python

"""
Build Generators:
Sum of integers
Doubler
Fibonacci sequence
Prime numbers
"""

def intsum(i=0):
    n = 0
    while True:
        yield i
        n += 1
        i += n

def intsum2(i=0):
    n = 0
    while True:
        yield i
        n += 1
        i += n

def doubler(i=1):
    while True:
        yield i
        i *= 2

def fib(i=0):
    j = 1
    while True:
        yield j
        h = i
        i = j
        j = h + i

def prime(i=2):
    while True:
        if i == 2 or 0 not in [i % x for x in range(2, i)]:
            yield i
        i += 1

def squared(i=0):
    while True:
        yield i ** 2
        i += 1

def cubed(i=0):
    while True:
        yield i ** 3
        i += 1

def threes(i=3):
    while True:
        yield i
        i += 3
        

from math import e

def exp(i=0):
    while True:
        yield i ** e
        i += 1

def negseven(i=0):
    while True:
        yield i
        i += -7

