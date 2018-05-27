
import math

def intsum():
    i = 0
    j = 0
    while True:
        yield i
        j += 1
        i += j


def intsum2():
    i = 0
    j = 0
    while True:
        yield i
        j += 1
        i += j


def doubler():
    i = 1
    while True:
        yield i
        i *= 2


def fib():
    i0 = 1
    i1 = 0
    i = i0
    while True:
        i = i0 + i1
        i0, i1 = i1, i
        yield i


def prime():
    n = 2
    while True:
        Iscomposite = False
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                Iscomposite = True
        if not Iscomposite:
            yield n
        n += 1
