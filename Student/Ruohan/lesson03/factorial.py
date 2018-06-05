#! /usr/local/bin/python3

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#compute factorial of 7
print(factorial(7))
