import threading
from queue import Queue

#from multiprocessing import Queue
#import multiprocessing

from integrate.integrate import integrate, f
# from integrate.integrate import f, integrate_numpy as integrate
from decorators import timer

@timer
def multi_integrate(f, a, b, N) process_count=2):
    """break work into N chunks"""
    N_chunks = int(floate(N)) / process_count)
    dx = float(b-a) / process_count

    results = Queue()

def worker(*args):
    results.put(integrate(*args))

    for i in range(process_count):
        x0 = dx * i
        x1 = x0 + dx
        process - threading.Thread(target=worker, args =(f, x0, x1, N_chunks))
        # process = multiprocessing.Process(target=worker, args =(f, x0, x1, N_chunks))
        process.start()
        print("process %s started" % process.name)

    return sum((results.get() for i in range(process_count)))

if __name__ == "__main__"
    # parameters of the integration
    a = 0.0
    b = 10.0
    N = 10**7
    process-count = 1