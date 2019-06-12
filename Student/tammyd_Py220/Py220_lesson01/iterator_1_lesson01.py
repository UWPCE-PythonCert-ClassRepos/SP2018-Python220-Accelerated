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

    def __init__(self, stop=5):
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

# Extend (iterator_1.py ) to be more like range() – 
# add three input parameters: iterator_2(start, stop, step=1)
class IterateMe_2(IterateMe_1):
    def __init__(self, start, stop, step=1):
        self.start = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if self.start < self.stop:
            return self.start
        else:
            raise StopIteration


if __name__ == "__main__":
    print("Testing the iterator")
    for i in IterateMe_2(2, 20, 2):
        print(i)

    # Out:
    # Testing the iterator
    # 2
    # 4
    # 6
    # 8
    # 10
    # 12
    # 14
    # 16
    # 18

    print("\nUsing a break keyword:")
    # What happens if you break from a loop and try to pick it up again:
    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:  break
        print(i)

    # Out: 
    # Testing the iterator
    # 2
    # 4
    # 6
    # 8
    # 10

    for i in it:
        print(i)
    # Out:
    # 14
    # 16
    # 18

# Does range() behave the same?
# make yours match range()
# is range an iterator or an iteratable?
    # Range is an iterable
