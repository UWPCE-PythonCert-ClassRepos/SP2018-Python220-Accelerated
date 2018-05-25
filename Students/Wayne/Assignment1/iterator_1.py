#!/usr/bin/env python

"""
Simple iterator examples
"""


class IterateMe_1:
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like range(4) )
    """

    def __init__(self, stop=10):
        self.current = -1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


class IterateMe_2:

    def __init__(self, start, stop, step):
        self.current = start - step
        self.stop = stop
        self.start = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


it = IterateMe_2(2, 20, 2)
for i in it:
    if i > 10:  break


def rng():
    print("Range function")
    for i in range(2, 20, 2):
        print(i)



if __name__ == "__main__":

    print("Testing the iterator")
    for i in IterateMe_1():
        print(i)

    print("Testing the IT iterator")
    for i in it:
        print(i)

rng()
