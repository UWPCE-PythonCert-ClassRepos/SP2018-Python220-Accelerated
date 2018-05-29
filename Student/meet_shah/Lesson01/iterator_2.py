#!/usr/bin/env python

"""
Extending Simple iterator to be more like range by adding more options
"""


class IterateMe_2:
    """
    Extending the simple iterator to allow you
    to configure start and increment values
    """

    def __init__(self, start=0, stop=0, increment=1):
        self.current = start - increment
        self.start = start
        self.stop = stop
        self.increment = increment

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.increment
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


if __name__ == "__main__":

    print("Testing simple iterator")
    for i in IterateMe_2(stop=5):
        print(i)

    print("Testing start and stop iterator")
    for i in IterateMe_2(10,15):
        print(i)

    print("Testing with increments")
    for i in IterateMe_2(10,15,2):
        print(i)
