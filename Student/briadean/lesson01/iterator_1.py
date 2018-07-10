#!/usr/bin/env python

"""
Revamped iterator examples
"""

class IterateMe:
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like range(4) )
    """

    def __init__(self, start, stop, step = 1):
        self.current = start - step
        self.start = start
        self.step = step
        self.stop = stop + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


if __name__ == "__main__":

    print("Testing the iterator")
    for i in IterateMe(2, 20, 2):
        print(i)
