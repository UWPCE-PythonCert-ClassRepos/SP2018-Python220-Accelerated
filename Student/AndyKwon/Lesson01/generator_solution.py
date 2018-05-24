

# class intsum():

#     def __init__(self, stop = 20)


def intsum():
    x = 0
    y = -1

    while True:
        y += 1
        x += y
        yield x

def doubler():
    x = 1

    while True:
        yield x
        x *= 2

def fib():
    x = 0
    y = 1

    while True:
        yield x
        x, y = y, x + y