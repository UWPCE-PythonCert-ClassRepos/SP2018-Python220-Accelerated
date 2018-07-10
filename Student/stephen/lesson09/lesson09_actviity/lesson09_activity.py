import threading
import time
import random

# simple threading
def func(n):
    for i in range(n):
        print('hello from thread %s' % threading.current_thread().name)
        time.sleep(random.random() * 2)


threads = []
for i in range(3):
    thread = threading.Thread(target=func, args=(i + 4,))
    thread.start()
    threads.append(thread)

# threads are not "blocking" eachother

# this code starts blocking the threads
for thread in threads:
    print("joining thread: ", thread.name)
    thread.join()

# this code is blocked before running
print("all threads finished")
# makes sure all the threads are finished before executing