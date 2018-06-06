# Andy K
# Lesson03
# Context Manager

""" 
Write a context manager class Locke to simulate the overall functioning of
the system. When the locke is entered it stops the pumps, opens the doors,
closes the doors, and restarts the pumps. Likewise when the locke is exited it
runs through the same steps: it stops the pumps, opens the doors, closes the
doors, and restarts the pumps. Don’t worry for now that in the real world there
are both upstream and downstream doors, and that they should never be opened at
the same time; perhaps you’ll get to that later. During initialization the
context manger class accepts the locke’s capacity in number of boats. If someone
tries to move too many boats through the locke, anything over its established
capacity, raise a suitable error. Since this is a simulation you need do nothing
more than print what is happening with the doors and pumps, like this:

"Stopping the pumps."
"Opening the doors."
"Closing the doors."
"Restarting the pumps."

This is how you might interact with your Locke class.

small_locke = Locke(5)
large_locke = Locke(10)
boats = 8

# Too many boats through a small locke will raise an exception
with small_locke as locke:
    locke.move_boats_through(boats)

# A lock with sufficient capacity can move boats without incident.
with large_locke as locke:
    locke.move_boats_through(boats)
"""


class Locke():

    def __init__(self, locke_capacity, handle_error=None):
        self.locke_capacity = locke_capacity
        self.handle_error = handle_error

    def __enter__(self):
        print("...Stopping Pumps...\n",
              "...Opening Gates...")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is AssertionError:
            self.handle_error = True
            print("%s\n" % (exc_value),
                  "...Closing Gates...\n"
                  "...Starting Pumps...")

            return self.handle_error

        print("...Closing Gates...\n",
              "...Starting Pumps...")
        return self.handle_error

    def boats_through_locke(self, num_boats):
        """
        compares Locke's capacity to the number of boats seeking passage
        """
        assert num_boats <= self.locke_capacity, (
            "Number of boats exceed locke capacity")

        print("Boats have passed through the locke")
