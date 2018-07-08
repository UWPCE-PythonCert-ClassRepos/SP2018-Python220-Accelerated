# Andy K
# Lesson03
# Recursion

"""
Write a recursive solution for the factorial function.
"""

def factorial(n):
    if n==1:
       return 1
    return n*factorial(n-1)


# simple asserts to test factorial values are equal to known values
assert factorial(1) == 1
assert factorial(4) == 24
assert factorial(5) == 120
assert factorial(20) == 2432902008176640000
