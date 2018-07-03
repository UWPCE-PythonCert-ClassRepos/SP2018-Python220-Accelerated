'''
  Notes for concurrency and async
'''


import sys
import threading
import time
from Queue import Queue

'''
    This is an intengration function
def f(x):
'''
    return x**2

def integrate(f, a, b, N):
    s = 0
    dx = (b-a)/N
    for i in xrange(N):
        s += f(a+i*dx)
    return s * dx

'''
    This starts threading
'''
def func():
    for i in xrange(5):
        print("hello from thread %s" % threading.current_thread().name)
        time.sleep(1)

threads = []
for i in xrange(3):
    thread = threading.Thread(target=func, args=())
    thread.start()
    threads.append(thread)

'''
    This is an example of subclassing
'''
class MyThread(threading.Thread):

    def run(self):
        print("hello from %s" % threading.current_thread().name)

thread = MyThread()
thread.start()

'''
    Mutex locks (threading.Lock)

        Probably most common
        Only one thread can modify shared data at any given time
        Thread determines when unlocked
        Must put lock/unlock around critical code in ALL threads
        Difficult to manage

    Easiest with context manager:
'''
x = 0
x_lock = threading.Lock()

# Example critical section
with x_lock:
    # statements using x


'''
    Locking threads
'''
lock = threading.Lock()

def f():
    lock.acquire()
    print("%s got lock" % threading.current_thread().name)
    time.sleep(1)
    lock.release()

threading.Thread(target=f).start()
threading.Thread(target=f).start()
threading.Thread(target=f).start()

'''
    This is a nonblocking locks
'''
lock = threading.Lock()
lock.acquire()
if not lock.acquire(False):
    print("couldn't get lock")
lock.release()
if lock.acquire(False):
    print("got lock")

'''
    Queueing
'''

#from Queue import Queue
q = Queue(maxsize=10)
q.put(37337)
block = True
timeout = 2
print(q.get(block, timeout))
