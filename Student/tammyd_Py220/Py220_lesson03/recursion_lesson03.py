#!usr/local/bin/python3

"""

Py220: Advanced Programming in Python
Lesson 03 Activity & Assignment: Recursion

Recursion

"""

# Write a recursive solution for the factorial function.

def factorial(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))


for i in range(0,10):
    print("Factorial of {} equals {}.".format(i, factorial(i)))