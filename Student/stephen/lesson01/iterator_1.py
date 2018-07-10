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

    def __init__(self, start, stop, step=1):
        self.current = start - step
        self.start = start
        self.stop = stop
        self.step = step

    
    # iterator version
    # def __iter__(self):
    #     return self
    
    # mimic range iterable
    def __iter__(self):
        self.current = self.start - self.step
        return self

    def __next__(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration



if __name__ == "__main__":

    print("Testing the iterator")
    it = IterateMe_1(0, 20, 1)
    for i in it:
        if i > 10:  break
        print(i)
    for i in it:
        print(i)
    
    print("Testing range")
    rg = range(0, 20, 1)
    for i in rg:
        if i > 10:  break
        print(i)
    for i in rg:
        print(i)

    print("Range objects are iterable; they do not keep track of state")
    
