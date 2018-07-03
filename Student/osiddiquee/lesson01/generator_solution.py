def intsum():
    previous, last = 0, 0
    while last >= 0:
        if last == 0:
            yield previous
            last += 1
        else:
            sum = previous + last
            previous = sum
            last += 1
            yield sum


def doubler():
    doubled = 1
    while doubled > 0:
        if doubled == 1:
            yield 1
            doubled *= 2
        elif doubled == 2:
            yield doubled
            doubled *= 2
        else:
            yield doubled
            doubled *= 2


def fib():
    first, second = 0, 1
    while first >= 0:
        if first == 0:
            yield second
            first = second
            second *= 2
        elif first == 1:
            yield first
            fib2 = second
            second = first + fib2
            first = fib2
        else:
            yield first
            fib2 = second
            second = first + fib2
            first = fib2


def prime():
    integer = 2
    while integer > 1:
        if integer == 2:
            yield integer
        else:
            isprime = True
            for i in range(2, integer):
                if integer % i == 0:
                    isprime = False
            if isprime:
                yield integer
        integer += 1
