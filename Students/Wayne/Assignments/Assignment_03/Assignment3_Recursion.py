# Finished inclass activity/assignment 

# Write a recursive solution for the factorial function.

# 5!=5x4x3x2x1=120

# n n!

# 0 1 1 1 2 2 3 6 4 24 5 120 6 720 7 5,040 8 40,320 9 362,880 10 3,628,800


def factorial(n):
    if n==1:
       return 1
    return n*factorial(n- 1)