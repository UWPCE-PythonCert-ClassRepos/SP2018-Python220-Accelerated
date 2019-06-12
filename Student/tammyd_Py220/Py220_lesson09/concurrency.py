import threading
import time
import random

# simple threading 

def func(n):
    for i in range(n):
        print("hello from thread %s" % threading.current_thread().name)
        time.sleep(random.random() * 2)

# run a bunch of fuctions at the same time
threads = []
for i in range(3):
    thread = threading.Thread(target=func, args=(i+2))
    thread.start()
    threads.append(thread)

# start and append thread. 
for thread in threads:
    print("Joining thread: ", thread.name)
    thread.join()
# to know when it is done
print("all threads finished.")

func(10)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`

# # race conditions

# import threading
# import time

# class shared:
#     val = 1

# def func():
#     y = shared.val
#     time.sleep(0.001)
#     y += 1
#     shared.val = y

# threads = []

# for i in range(100):
#     thread = threading.Thread(target=func)
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

# print(shared.val)



