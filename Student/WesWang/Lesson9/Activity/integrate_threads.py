import threading
import queue
import time

#from integrate import integrate, f
from integrate import f, integrate_numpy as integrate


def threading_integrate(f, a, b, N, thread_count=2):
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
    a = 0.0
    b = 10.0
    N = 10**7
    thread_count = 1

    start = time.time()
    print("Numerical solution with N=%(N)d : %(x)f" %
            {'N' : N, 'x' : threading_integrate(f, a, b, N, thread_count=thread_count)}) 
    end = time.time()
    print("Time elapsed:", end-start)