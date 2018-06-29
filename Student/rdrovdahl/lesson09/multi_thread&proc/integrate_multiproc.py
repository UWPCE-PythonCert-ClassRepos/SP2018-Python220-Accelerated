#!/usr/bin/env python3

'''
Program that calls the computation functions in integrate.py and allows
multiprocessing based on the proc_count variable in __main__
'''

# import threading
# import queue
import time
from multiprocessing import Queue
import multiprocessing


## comment out either integrate or integrate_numpy depending on which API you
## want to test

from integrate import integrate, f
# from integrate import f, integrate_numpy as integrate

# from decorators import timer  ## this didn't work, ned to investigate.  Added a timer to main instead



# @timer
def multi_integrate(f, a, b, N, process_count=2):
    """break work into N chunks"""
    N_chunk = int(float(N) / process_count)
    dx = float(b - a) / process_count

    results = Queue()

    def worker(*args):
        results.put(integrate(*args))

    for i in range(process_count):
        x0 = dx * i
        x1 = x0 + dx
        process = multiprocessing.Process(target=worker, args=(f, x0, x1, N_chunk))
        process.start()
        print("process %s started" % process.name)

    return sum((results.get() for i in range(process_count)))


if __name__ == "__main__":

    # parameters of the integration
    a = 0.0
    b = 10.0
    N = 10**8
    process_count = 16

    begin = time.time()
    print("Numerical solution with N=%(N)d : %(x)f" %
          {'N': N, 'x': multi_integrate(f, a, b, N, process_count=process_count)})
    end = time.time()
    print('it took: ', end - begin, 'seconds')
