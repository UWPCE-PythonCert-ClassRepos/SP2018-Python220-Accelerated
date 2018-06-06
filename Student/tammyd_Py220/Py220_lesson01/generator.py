#!/usr/local/bin/python3

"""
Py220: Advanced Python
Lesson 01

Generators
"""


# Write a few generators:
# generator format:
# def a_generator_function(params):
#     some_stuff
#     yield something


# Sum of integers
def intsum(x=0, sum=0):
    while True:
        sum += x
        yield sum
        x += 1

sum_int = intsum()
print(next(sum_int))




# Doubler
def doubler(x=1):
    while True:
        yield x
        x = x*2

sum_doubler = doubler()
print(next(sum_doubler))




# Fibonacci sequence
def fib(a=1, b=1):
    while True:
        yield a 
        a, b = b, a+b

fib_num = fib()
print(next(fib_num))

print()



# # Prime numbers
def prime(x=2):
    while True:
        if not [val for val in range(2, x) if x % val == 0]:
            yield x
        x += 1

# My incorrect try. Yielding all odds. How can I edit to yield just primes?

# def prime(x=1):
#    if x == 2:
#        yield x
#    while True:
#        if x % 2 != 0:
#            yield x
#            x += 1
#        else:
#            x += 1

prime_num = prime()
print(next(prime_num))
print(next(prime_num))
print(next(prime_num))
print(next(prime_num))
print(next(prime_num))
print(next(prime_num))
print(next(prime_num))






