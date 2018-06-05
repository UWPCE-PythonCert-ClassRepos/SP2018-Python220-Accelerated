#! /usr/local/bin/python3

class Locke(object):

    def __init__(self, num, error = None):
        self.capacity = num
        self.handle_error = error

    def __enter__(self):
        if not self.handle_error:
            print("Stopping the pumps.\nOpening the doors.\nClosing the doors.\nRestarting the pumps.\n")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.handle_error:
            print("Stopping the pumps.\nOpening the doors.\nClosing the doors.\nRestarting the pumps.\n")
        return self.handle_error

    def move_boats_through(self, boats):
        if boats > self.capacity:
            raise ValueError('The boats beyoned the capacity')
        else:

            return self


small_locke = Locke(5)
large_locke = Locke(10)
boats = 8

# Too many boats through a small locke will raise an exception
with small_locke as locke:
    locke.move_boats_through(boats)

# A lock with sufficient capacity can move boats without incident.
with large_locke as locke:
    locke.move_boats_through(boats)
