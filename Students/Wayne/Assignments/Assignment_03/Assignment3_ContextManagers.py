# canvas submitting version

class Locke():
    def __init__(self, boats, locke=None, error=None):
        self.boats = boats
        self.locke = locke
        self.error = error

    def __enter__(self):
        if not self.error:
            print('''Lock Status:
                          Stopping the pumps
                          Opening the doors
                          Closing the doors
                          Starting the pumps
                ''')
        return self

    def move_boats_through(self, boats, locke):

        if self.boats > self.locke:
            raise ValueError('Too many boats for the locks')
        else:
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.error:
            print('''Lock Status:
                          Stopping the pumps
                          Opening the doors
                          Closing the doors
                          Starting the pumps
                ''')
        return self.error