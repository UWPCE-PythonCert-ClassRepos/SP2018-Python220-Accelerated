#!usr/local/bin/python3

"""

Py220: Advanced Programming in Python
Lesson 03 Activity & Assignment: Context Managers

Context Managers

"""



# During initialization the context manger class accepts the locke’s capacity in number of boats. 
# If someone tries to move too many boats through the locke, anything over its established capacity, raise a suitable error. 

class Locke:

    def __init__(self, boats):
        self.boats = boats
    
    # When the locke is entered it stops the pumps, opens the doors, closes the doors, and restarts the pumps. 
    def __enter__(self):
        return self

    # when the locke is exited it runs through the same steps: it stops the pumps, opens the doors, closes the doors, and restarts the pumps. 
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__({}, {}, {})".format(exc_type, exc_val, exc_tb))
        return self

    def move_boats_through(self, num_boats):
        # If someone tries to move too many boats through the locke, anything over its established capacity, raise a suitable error. 
        if num_boats > self.boats:
            raise ValueError("Too many boats. {} boats is more than the {} boat capacity.".format(num_boats, self.boats))
        else:
            print("Moving boats through. \n" \
                  "Stopping the pumps. \n" \
                  "Opening the doors. \n" \
                  "Closing the doors. \n" \
                  "Restarting the pumps.")


if __name__ == '__main__':
    # capacity of the small locke is 5 boats
    small_locke = Locke(5)
    # capacity of the large locke is 10 boats
    large_locke = Locke(10)
    # attempting to pass through 8 boats 
    # boats = 8

    with small_locke as locke:
        print("Small boat:")
        locke.move_boats_through(5)



    with large_locke as locke:
        print("\nLarge boat:")
        locke.move_boats_through(8)

    with large_locke as locke:
        print("\nLarge boat:")
        locke.move_boats_through(18)


