
class Locke:

    def __init__(self, locke_capacity = 10, handle_error = None):
        self.locke_capacity = locke_capacity
        self.handle_error = handle_error

    def __enter__(self):
        if not self.handle_error:
            print('Stopping the pumps.\n',
                   'Opening the doors.\n')

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.handle_error:
            print('Closing the doors.\n',
                  'Restarting the pumps.\n')

        return self.handle_error

    def move_boats_through(self, number_boats):
        if number_boats <= self.locke_capacity:
            print('Boats have moved through')
        else:
            raise RuntimeError('The number of boats is too damn high')
        return self
