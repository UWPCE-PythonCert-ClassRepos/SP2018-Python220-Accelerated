#! /usr/bin/env python3
def factorial(n):
    if n == 1:
        return n
    else:
        a = n * factorial(n-1)
        return a

print('Factorial 5 is {}'.format(factorial(5)))
