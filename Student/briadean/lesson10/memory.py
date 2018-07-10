"""
Script to demonstrate the memory_profiler functionality
Requires pip install -U memory_profiler
To run without decorator, run python -m memory_profiler example.py
To be able to use decorator, must import from memory_profiler import profile, run python example.py
Will print line by line memory usage to stout
This can help you determine specifically which line/lines are consuming the most memory in the event that memory for
    your project is restricted
The module also has the ability to display
"""
from memory_profiler import profile

"""
@profile decorator can be used to mark functions that you would like to profile.
"""


@profile(precision=4)
def fibonacci1(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a + b
    return a


if __name__ == "__main__":

    for i in range(1, 10):
        print(fibonacci1(i))

