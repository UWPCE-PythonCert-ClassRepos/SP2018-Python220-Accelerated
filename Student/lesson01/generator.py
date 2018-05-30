'''
Jay Johnson - Lesson01 - Activity01 - Generators
'''
import math
### generator ####

#0, 1, 3, 6, 10, 15
# Sum of the integers
def sum_range(start, stop, step=1):
    i = start
    k = 1
    print(i)
    while i < stop:
        yield i + k
        i += step
        k = i + k

#  Doubler 1, 2, 4, 8, 16, 32,
def y_range(start, stop, step=1):
    i = start
    while i < stop:
        yield i
        i += i
        i += step
        step = 0


# Fibonacci sequence
def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b


# Prime numbers
def prime():
    noprimes = [j for i in range(2, 8) for j in range(i*2, 24, i)]
    primes = [x for x in range(2, 24) if x not in noprimes]
    print(primes)


if __name__ == '__main__':

    sum_number = sum_range(0, 10, step=1)

    #gernerator for sum of ints
    for s_number in sum_number:
        print(s_number)

    print('\n break \n')

    y_ranger = y_range(0, 33, step=1)

    # generator for doubler
    for y_number in y_ranger:
        print(y_number)

    print('\n break \n')

    # generator of fibonacci numbers
    fibonacci_generator = fibonacci(35)

    # print out the fibonacci numbers
    for fibonacci_number in fibonacci_generator:
        print(fibonacci_number)

    print('\n break \n')

    prime()
