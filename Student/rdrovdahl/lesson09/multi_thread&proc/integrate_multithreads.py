#!/usr/bin/env python3

'''
Program that calls the computation functions in integrate.py and allows
multithreading based on the thread_count variable in __main__
'''

import threading
import queue
import time

## comment out either integrate or integrate_numpy depending on which API you
## want to test

# from integrate import integrate, f
from integrate import f, integrate_numpy as integrate

# from decorators import timer  ## this didn't work, ned to investigate.  Added a timer to main instead



# @timer
def threading_integrate(f, a, b, N, thread_count=2):
    """break work into N chunks"""
    N_chunk = int(float(N) / thread_count)
    dx = float(b - a) / thread_count

    results = queue.Queue()

    def worker(*args):
        results.put(integrate(*args))

    for i in range(thread_count):
        x0 = dx * i
        x1 = x0 + dx
        thread = threading.Thread(target=worker, args=(f, x0, x1, N_chunk))
        thread.start()
        print("Thread %s started" % thread.name)

    return sum((results.get() for i in range(thread_count)))


if __name__ == "__main__":

    # parameters of the integration
    a = 0.0
    b = 10.0
    N = 10**8
    thread_count = 4

    begin = time.time()
    print("Numerical solution with N=%(N)d : %(x)f" %
          {'N': N, 'x': threading_integrate(f, a, b, N, thread_count=thread_count)})
    end = time.time()
    print('it took: ', end - begin, 'seconds')
