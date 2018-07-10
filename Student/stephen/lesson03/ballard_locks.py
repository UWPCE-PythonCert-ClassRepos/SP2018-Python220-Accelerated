# Sequence:
# "Stopping the pumps."
# "Opening the doors."
# "Closing the doors."
# "Restarting the pumps."



class Locke(object):
    """
    From Doug Hellmann, PyMOTW
    https://pymotw.com/3/contextlib/#module-contextlib
    """

    def __init__(self, boat_limit):
        self.boat_limit = boat_limit

    def move_boats_through(self, boats):
        if boats > self.boat_limit:
            raise RuntimeError('Too many boats!')
        else:
            print('Opening the doors.')

    def __enter__(self): 
        print('Stopping the pumps.')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is RuntimeError:
            print(exc_val)
        else:
            print('Closing the doors.')
            print('Restarting the pumps.')
        return self

small_locke = Locke(5)
large_locke = Locke(10)
boats = 8

# Too many boats through a small locke will raise an exception
print('Testing small_locke using 8 boats.')
with small_locke as locke:
    locke.move_boats_through(boats)

# A lock with sufficient capacity can move boats without incident.
print('Testing large_locke using 8 boats.')
with large_locke as locke:
    locke.move_boats_through(boats)

# Results:
# Testing small_locke using 8 boats.
# Stopping the pumps.
# Too many boats!
# Testing large_locke using 8 boats.
# Stopping the pumps.
# Opening the doors.
# Closing the doors.
# Restarting the pumps.