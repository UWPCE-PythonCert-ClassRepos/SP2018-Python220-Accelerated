'''
async def corout():
    print("running corout")
    return "something returned"

async def corout2():
    print("running corout2")
    await corout()

cr = corout()
cr.send(None)

cr2 = corout2()
cr2.send(None)
'''
from types import coroutine
'''
@coroutine
def do_nothing():
    yield "something from do_nothing"

dn = do_nothing()
dn.send(None)
dn.send(None)

async def do_a_few_things(num=3):
    for i in range(num):
        print(f"in the loop for the {i}th time")
        res = await do_nothing()
        print("res is:", res)
    return "do a few things result"

daft = do_a_few_things(5)
# daft.send(None)

while True:
    try:
        daft.send(None)
    except StopIteration as si:
        print("The awaitable is complete")
        print("passed out:", si)
        break

Generator
def gen():
    for i in range(3):
        res = yield i
        print(f"loop: {i}, result: {res}")
    return "returned from gen"

g = gen()
'''

print("\n\n***************\n\n")

@coroutine
def nothing():
    yield "from nothing"
    return "returned from nothing"

@coroutine
def count(num):
    for i in range(num):
        yield f"count: {i}"

async def do_a_few_things(num=3, name="no_name"):
    for i in range(num):
        print(f'in the "{name}" loop for the {i}th time')
        from_await = await nothing()
        print("value returned from await:", from_await)

daft = do_a_few_things(5, "first one")
daft.send(None)

i = 0
while True:
    i += 1
    print(f"\n{i}th time in the outer while loop")
    try:
        res = daft.send(i)
        print("result of send:", res)
    except StopIteration:
        print("The awaitable is complete")
        break

print("\n\n***************\n\n")

@coroutine
def nothing():
    yield "yielded from nothing"
    return "returned from nothing"


@coroutine
def count(num):
    for i in range(num):
        yield f"count: {i}"
    return "returned from count"


async def do_a_few_things(num=3, name="no_name"):
    for i in range(num):
        print(f'in the "{name}" loop for the {i}th time')
        from_await = await count(i + 2)
        print("value returned from await:", from_await)


class TaskLoop():

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def run_all(self):
        i = 0
        while self.tasks:
            i += 1
            print(f"\nOuter loop count: {i}")
            task = self.tasks.pop()
            try:
                res = task.send(None)
                print("result of send:", res)
                self.tasks.insert(0, task)
            except StopIteration:
                print("The awaiable is complete")
                # break

print("\n\n*** Running the Loop class\n")

loop = TaskLoop()
loop.add_task(do_a_few_things(2, "first task"))
loop.add_task(do_a_few_things(4, "second task"))
loop.add_task(do_a_few_things(3, "third task"))

loop.run_all()

import time

@coroutine
def sleep(secs=0):
    start = time.time()
    yield "{} seconds have passed".format(time.time() - start)
    while time.time() - start < secs:
        yield "yielding in sleep"
    return "{} seconds have passed".format(time.time() - start)

async def fib(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
        await sleep(0.1)
        return b


class TaskLoop2():

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def run_all(self):
        results = []
        i = 0
        while self.tasks:
            i += 1
            time.sleep(0.001)
            print(f"\nOuter loop count: {i}")
            task = self.tasks.pop()
            try:
                res = task.send(None)
                print("result of send:", res)
                self.tasks.insert(0, task)
            except StopIteration as si:
                results.append(si.args[0])
        return results


print("\n\n***Running the Loop with fibbonacci number\n")

loop = TaskLoop2()
loop.add_task(fib(3))
loop.add_task(fib(5))
loop.add_task(fib(7))
loop.add_task(fib(10))
loop.add_task(fib(4))
loop.add_task(fib(6))

start = time.time()
results = loop.run_all()
print(f"total run time: {time.time() - start} seconds")

print("the results are:", results)

