#! /usr/local/bin/python3


def fibonacci(n):
    '''
    This function will return the 'n'th value in the fibonacci series.
    The starting elements in the series are 0, 1.
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    '''
    This function returns the 'n'th value in the lucas series
    The starting elements in the series are 2, 1.
    '''
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, a=0, b=1):
    '''
    This function returns the 'n'th value in a fibonacci type sequence that can
    have customizable values for the first two series positions.
    By default, the starting elements in the series are 0, 1.
    By supplying the optional arguments to the function, the first two values
    can be defined as desired.
    '''
    if n == 0:
        return a
    if n == 1:
        return b
    else:
        return sum_series(n-1, a, b) + sum_series(n-2, a, b)


# There are 3 variables that are used as the functions are called which can be
# modified as desired.
# 'x' is the series element that the function will return the value for
# 'a' = value of the first element in the series for the sum_series function
# 'b' = value of the second element in the series for the sum_series function

x = 50
a = 0
b = 1

print('Function: fibonacci\nSeries Element:', x, '\nValue:', fibonacci(x), '\n')
# print('Function: lucas\nSeries Element:', x, '\nValue:', lucas(x), '\n')
# print('Function: sum_series\nSeries Element:', x, '\nFirst Two Values:', a, b, '\nValue:', sum_series(x), '\n')


# All assertion testing will be accomplished by comparig the 10th element of
# the series functions.
#
# The first assertion test shows that the fibronacci function is returning
# correct values.  The 10th element of a fibronacci series = 55.  If the
# fibonacci fucntion is returning anything other than 55, an Assertion error
# will be generaged below.
# assert (fibonacci(10) == 55)

# The second assertion test shows that the lucas function is returning
# correct values.  The 10th element of a lucas series = 123.  If the
# lucas fucntion is returning anything other than 123, an Assertion error
# will be generaged below.
# assert (lucas(10) == 123)

# The third assertion tests shows that the sum_series function is returning
# correct values.  The 10th element of a sum_series series with default values
# for the first two elements (0, 1) = 55 which matches the fibronacci function.
# If we set the optional arguments for the first to elements to '1,2', we'll
# match the output of the lucas function which is 123.
# If the sum_series fucntion is returning anything other than the expected
# results, an Assertion error will be generaged below.
# assert (sum_series(10) == 55)
# assert (sum_series(10, 2, 1) == 123 == lucas(10))
