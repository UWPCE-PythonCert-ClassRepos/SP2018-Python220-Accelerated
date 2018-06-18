#!/usr/bin/env python3
"""
Generators
intsum - return sum of two integers by adding the next int
intsum2 - return sum of two integers by adding the next int (used optional parameters, allows user to define starting point and step size)
doubler - start with 1, return double each time
fib - return next in the fibonacci sequence
prime - return next prime
"""

def intsum():
    input1 = 0
    input2 = 0
    while True:
        yield input1
        input2 += 1
        input1 += input2


def intsum2(input1=0,input2=0):
    while True:
        yield input1
        input2 += 1
        input1 += input2


def doubler(start=1):
    while True:
        yield start
        start *= 2

def fib(input1=0, input2=1):
    i = input2
    while True:
        yield i
        i = input1 + input2
        input1 = input2
        input2 = i


def check_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

def prime(start=2):
    while True:
        if check_prime(start):
            yield start
        start +=1
