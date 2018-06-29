## start with this ...

## make decorators.py file

def add(x,y):
	return x+y

def sub(x,y):
	return x-y

def mul(x,y):
	return x*y

### calling this in the repl

>>> import decorators.py


## Add prints

def add(x,y):
	print("Calling add")
        return x+y

def sub(x,y):
	print("Calling sub")
        return x-y

def mul(x,y):
    print("Calling mul")
	return x*y

### calling this in the repl

>>> import decorators.py

## Now, you have to do something else or change all these edtis,
## we would have to go back and change our code in 100s of place

## this is turning into a maintenance nightmare
## also the code is repeated - which goes against the concept of programming

## Lets take this code and generalize this

## You are going to give me a function and I will write a wrapper around it

## file name logcall.py

def logged(func):
	# adding logging
	def wrapper(*args, **kwargs):
		print('Calling', func.__name__)
		return func(*args, **kwargs)
	return wrapper

## Once that is done, then
## import the logcall.py

## create decorators.py file

from logcall import logged

add = logged(add)
sub = logged(sub)

## loging has been isolated in place
## but we have manually wrap the logged function
## like this


def add(x,y):
    return x+y
add=logged(add)

def sub(x,y):
        return x-y
sub=logged(sub)

def mul(x,y):
        return x*y
mul=logged(mul)

## this is the idea behind decoration
## go back to theory and then come to next phase -


## This is still not ideal as we would have to do this for all our n number
## of functions

def add(x,y):
        return x+y
add=logged(add)

## can be turned into

@logged
def add(x,y):
        return x+y

## we would have to add @logged for all the 500 functions ....
## These wrapper functions we create do not look anything else original
## functions - # type this

>>> decorators.add
>>> decorators.sub
>>> help (decorators.add)

## it doesn't show anything about the original function - just says wrapper.

## So, when you define a wrapper, you need to get some documentation over
## from original function

## This is done using wraps from functools.
## so in the logcall.py, add wraps at the top

from functools import wraps

@wraps(func)
def logged(func):
        # adding logging
        def wrapper(*args, **kwargs):
                print('Calling', func.__name__)
                return func(*args, **kwargs)

        return wrapper

## end logcall file

## adding wraps is equivilant to
## wraper.__name__=func.__name__
## wrapper.__doc__=func.__doc__

## now try

>>> decorators.add
>>> decorators.sub
>>> help (decorators.add)
