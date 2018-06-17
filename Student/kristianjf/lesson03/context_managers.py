#! /usr/bin/env python3
from contextlib import contextmanager
'''Build locke system for US Army Corps.
Use context managers to ensure state is properly captured upon entry and released upon exit'''

class Locke:
    def __init__(self, locke_size, num_boats=None, handle_error=None):
        self.locke_size = locke_size
        self._num_boats = num_boats
        self._handle_error = handle_error
    def move_boats_through(self, num_boats):
        if self._num_boats is not None:
            num_boats += self._num_boats
        assert num_boats < self.locke_size, ('Number of boats exceeded the locke size')
        self._num_boats = num_boats
    def __enter__(self):
        print('''Stopping the pumps.
        Opening the doors.
        Closing the doors.
        Restarting the pumps.''')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is AssertionError:
            self._handle_error = True
            print('__exit__({}, {}, {})'.format(exc_type, exc_val, exc_tb))
            return self._handle_error
        print('''Stopping the pumps.
        Opening the doors.
        Closing the doors.
        Restarting the pumps.''')
        return self._handle_error
