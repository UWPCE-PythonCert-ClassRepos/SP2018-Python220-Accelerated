import threading
import time

class shared:
    val = 1

def func():
    y = shared.val
    time.sleep(0.001)
    y += 1
    shared.val = y

threads = []

for i in range(100):
    thread = threading.Thread(target=func)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(shared.val)

