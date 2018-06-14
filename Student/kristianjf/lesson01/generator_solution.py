#!/usr/bin/env python3

def intsum(a=(x for x in range(0,6))):
    n = 0
    for i in a:
        n += i
        yield n


def doubler(a=(x for x in range(0,16))):
    for i in a:
        yield 2**i

def fib_func(n, s0=0, s1=1):
    if n < 0:
        return None
    if n == 0:
        return s0
    elif n == 1:
        return s1
    return fib_func(n - 1, s0, s1) + fib_func(n - 2, s0, s1)

def fib(n=20):
    for i in range(1, n):
        yield fib_func(i)

def prime_func(i=0):
    # is i a prime number?
    # if it can only be divided by itself and 1 and return a remainder of 0 for numbers from 1 to i
    if i > 1 and i % 1 == 0 and i % i == 0:
        for n in range(1, i-1):
            n += 1
            if i % n == 0:
                return False
        return True
    else:
        return False

def prime(a=1):
    while True:
        a += 1
        if prime_func(a):
            yield a
