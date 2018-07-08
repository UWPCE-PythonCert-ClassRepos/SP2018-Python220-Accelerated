import threading
import time
import random

"""
threading practice
"""

# def func():
#     for i in range(5):
#         print("hello from thread %s" % threading.current_thread().name)
#         time.sleep(random.random() *2)

# threads = []
# for i in range (3):
#         thread = threading.Thread(target=func, aergs())
#         thread.start()
#         threads.append(thread)

# for thread in threads:
#     print("joining thread:", thread.name)
#     thread.join()
#     print("all threads finished")

# for thread in threads:
#     thread.join()

def doubler(num):
    print(thread.currentThread().getname())
    print((num * 2) + '/n')

for i in range(5):
    thread = threading.Thread(target=doubler, args=(i, ))
    thread.start
    