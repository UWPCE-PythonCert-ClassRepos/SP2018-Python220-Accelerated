

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

def prime():
    x = 0

    while True:
        if x == 0:
            yield x
        elif x == 1:
            yield x
        elif x == 2:
            yield x
        elif x == 3:
            yield x
        elif x == 5:
            yield x
        elif x == 7:
            yield x
        elif x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
            yield x

        x += 1

