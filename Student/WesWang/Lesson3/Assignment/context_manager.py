class Locke:
  def __init__(self, capacity, boats=None, error=None):
    self.capacity = capacity
    self.boats = boats
    self.error = error

  def move_boats_through(self, boats):
    if boats > self.capacity:
      raise ValueError("Too many boats!") 

  def __enter__(self):
    print('''"Stopping the pumps."
  "Opening the doors."
  "Closing the doors."
  "Restarting the pumps."''')
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    if exc_type is ValueError:
      print('__exit__({}, {}, {})'.format(exc_type, exc_val, exc_tb))
      return self.error
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