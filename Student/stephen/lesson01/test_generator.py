"""
test_generator.py

tests the solution to the generator lab

can be run with py.test or nosetests
"""

import generator_solution as gen
from math import e


def test_intsum():

    g = gen.intsum()

    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 3
    assert next(g) == 6
    assert next(g) == 10
    assert next(g) == 15


def test_intsum2():

    g = gen.intsum2()

    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 3
    assert next(g) == 6
    assert next(g) == 10
    assert next(g) == 15


def test_doubler():

    g = gen.doubler()

    assert next(g) == 1
    assert next(g) == 2
    assert next(g) == 4
    assert next(g) == 8
    assert next(g) == 16
    assert next(g) == 32

    for j in range(10):
        j = next(g)

    assert j == 2**15


def test_fib():
    g = gen.fib()
    assert [next(g) for i in range(9)] == [1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_prime():
    g = gen.prime()
    for val in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        assert next(g) == val

def test_squared():
    g = gen.squared()
    for val in [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]:
        assert next(g) == val


def test_cubed():
    g = gen.cubed()
    for val in [0, 1, 8, 27, 64, 125, 216]:
        assert next(g) == val

def test_threes():
    g = gen.threes()
    for val in [3, 6, 9, 12, 15, 18, 21]:
        assert next(g) == val


def test_exp():
    g = gen.exp()
    for val in [0 ** e, 1 ** e, 2 ** e, 3 ** e, 4 ** e, 5 ** e, 6 ** e]:
        assert next(g) == val

def test_negseven():
    g = gen.negseven()
    for val in [0, -7, -14, -21, -28, -35, -42]:
        assert next(g) == val
