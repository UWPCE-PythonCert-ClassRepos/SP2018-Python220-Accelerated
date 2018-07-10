#!/usr/bin/env python3

'''
Some experimental code working with coroutines by themselves, outside of an
async framework or event loop.
'''


# note - using the async keyword makes this function a coroutine
async def corout():
    print('running corout')
    return 'something returned'

# Note that the returned value gets tacked on to the StopIteration

async def corout2():
    print('running corout2')
    await corout()


# You can also create coroutines by using the coroutine decorator from the
# types module

from types import coroutine

'''
applying the coroutine decorator makes a generator a coroutine, and thus an async...
'''

@coroutine
def do_nothing():
    '''
    Here is one that does absolutely nothing
    but it can be awaited
    '''
    yield 'something from do_nothing()'


# Another example of a coroutine that awaits on the first one

async def do_a_few_things(num=3):
    # a loop for multiple things
    for i in range(num):
        print(f'in the loop for the {i}th time')
        res = await do_nothing()
        print('res is:', res)

daft = do_a_few_things()
# daft.send(None)

while True:
    try:
        daft.send(None)
    except StopIteration:
        print('The awaitable is complete')
        break


'''
now we have what we need to make something that might look a bit like a task
loop
'''
print('\n\n*************\n\n')

@coroutine
def nothing():
    yield 'yielded from nothing'
    return ('returned from nothing')

@coroutine
def count(num):
    for i in range(num):
        yield f'count: {i} from the inner loop'
    return 'returned from count'

async def do_a_few_things(num=3, name='no_name'):
    for i in range(num):
        print(f'in the '{name}' middle loop for the {i}th time')
        from_await = await count(i + 2)
        print('value returned from await:', from_await)

# we're going to create a class to make a task loop
class TaskLoop():
    def __init__(self):
        # list to hold the tasks
        self.tasks = []

    def add_task(self, task):
        # add a task to the loop task must be a coroutine
        self.tasks.append(task)

    def run_all(self):
        # this is where the task loop runs
        # keep a loop going until all the tasks are gone
        i = 0
        while self.tasks:
            i += 1
            print(f'\nOuter loop count: {i}')
            # pop a task off the end
            task = self.tasks.pop()
            # run that task
            try:
                res = task.send(None)
                print('result of send:', res)
                #put it back on the beginning of the task list
                self.tasks.insert(0, task)
            except StopIteration:
                # this will be raised if it is done
                # so we don't put it back on the task list
                print('The awaitable is complete')

print('\n\n*** Running the Loop class\n')

# to use it we create a task loop object and add tasks to it
loop = TaskLoop()
loop.add_task(do_a_few_things(2, 'first task'))
loop.add_task(do_a_few_things(4, 'second task'))
loop.add_task(do_a_few_things(3, 'third task'))

# and then call run_all
loop.run_all()
