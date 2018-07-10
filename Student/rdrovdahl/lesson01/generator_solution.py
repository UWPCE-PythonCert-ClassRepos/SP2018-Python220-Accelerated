#! /usr/local/bin/python3


'''
A few simple generators
'''


def intsum():
    'generator to keep adding the next integer'
    i = 0
    current_value = 0
    while True:
        yield current_value
        i += 1
        current_value += i


def intsum2():
    'generator to keep adding the next integer'
    i = 0
    current_value = 0
    while True:
        yield current_value
        i += 1
        current_value += i


def doubler():
    'generator to keep doubling the value'
    current_value = 1
    while True:
        yield current_value
        current_value *= 2


def fib():
    'finonacci series generator'
    a = 1
    b = 1
    while True:
        yield a
        a, b = b, a + b


def prime():
    'generate all prime numbers between 2-100'
    while True:
        for i in range(2, 101):
            prime = True
            for x in range(2, i):
                if i % x == 0:
                    prime = False
            if prime is True:
                yield i
