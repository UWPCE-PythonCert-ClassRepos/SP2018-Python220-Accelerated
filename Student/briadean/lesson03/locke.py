#! /usr/local/bin/python3

"""
Software control system for Ballard Locks commissioned by Army Corps of Engineers
"""


class Locke:
    def __init__(self, locke_cap, num_boats=None, locke_error=None):
        self.locke_cap = locke_cap
        self.num_boats = num_boats
        self.locke_error = locke_error

    def __enter__(self):
        print("Stopping the pumps.\n"
              "Opening the doors.\n")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.locke_error:
            print("Closing the doors.\n"
                  "Restarting the pumps.\n")
            return self.locke_error

    def move_boats_through(self, num_boats):
        if num_boats <= self.locke_cap:
            print("Boats are successfully through the lock!\n")
        else:
            raise ValueError("Too many boats!\n")
        return self


small_locke = Locke(5)
large_locke = Locke(10)
boats = 8

with large_locke as lock:
    lock.move_boats_through(boats)

# AttributeError: 'NoneType' object has no attribute 'move_boats_through' for line 37. I honestly don't understand
# how how that function is not an attribute :(
