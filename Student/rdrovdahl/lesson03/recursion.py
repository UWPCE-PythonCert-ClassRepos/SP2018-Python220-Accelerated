#! /usr/local/bin/python3


'Write a recursive solution for the factorial function.'


def factorial(num):
    if num == 1:
        return 1
    else:
        f = num * factorial(num-1)
        return f

x = factorial(10)
print(x)
