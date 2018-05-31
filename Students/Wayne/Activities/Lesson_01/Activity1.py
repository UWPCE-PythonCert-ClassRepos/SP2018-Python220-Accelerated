
# coding: utf-8

# # Iterators and Iterables

# In[1]:


class IterateMe_1:
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like range(4) )
    """

    def __init__(self, stop=10):
        self.current = -1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


class IterateMe_2:

    def __init__(self, start, stop, step):
        self.current = start - step
        self.stop = stop
        self.start = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


it = IterateMe_2(2, 20, 2)
for i in it:
    if i > 10:  break


def rng():
    print("Range function")
    for i in range(2, 20, 2):
        print(i)


# In[2]:


if __name__ == "__main__":

    print("Testing the iterator")
    for i in IterateMe_1():
        print(i)

    print("Testing the IT iterator")
    for i in it:
        print(i)

rng()


# is range an iterator or an iteratable? Range is an interables, because you cannot call next on range. An iterator will change the state of the objects in the sequence.

# # GENERATOR

# Sum of the integers:
# 
# keep adding the next integer
# 
# 0 + 1 + 2 + 3 + 4 + 5 + …
# 
# so the sequence is:
# 
# 0, 1, 3, 6, 10, 15 …..

# In[ ]:


def sum_fun():
        for n in range(1,6,1):
            yield n*(n+1)/2
            
sum_it = (sum_fun())


# In[ ]:


list(sum_it)


# Doubler:
# 
# Each value is double the previous value:
# 
# 1, 2, 4, 8, 16, 32,

# In[ ]:


def doubler():
        for n in range(1,7,1):
            yield (n+1)*2
            
        
double_it = (doubler())


# In[ ]:


list(double_it)


# Fibonacci sequence:
#     
# The Fibonacci sequence as a generator:
# 
# f(n) = f(n-1) + f(n-2)
# 
# 1, 1, 2, 3, 5, 8, 13, 21, 34…

# Generate the prime numbers (numbers only divisible by them self and 1):
# 
# 2, 3, 5, 7, 11, 13, 17, 19, 23…

# # Calculator Exercise
# 

# This is the functional vs imperative exervise

# In[ ]:


OPERATORS = '+', '-', '*', '/'


def p_main():
   
   """The main flow."""

   print('Welcome to the barely functional calculator!')
   number1 = p_get_number()
   operator = p_get_operator()
   number2 = p_get_number()
   result = p_calculate(number1, operator, number2)
   print('The result is: %s' % result)


def p_get_number():
   
   """Reads an integer from the standard input and returns it.
   If a non-integer value is entered, a warning is printed,
   and a new value is read."""
           
   while True:
       s = input('Enter an integer: ')
       try:
           return int(s)
       except ValueError:
           print('That is not an integer!')
           

def p_get_operator():
   
   """Reads an operator from the standard input and returns it.
   Valid operators are: +, -, *, and /. If an invalid operator
   is entered, a warning is printed, and a new value is read."""    
   
   while True:
       s = input('Enter an operator (+, -, *, or /): ')
       if s in OPERATORS:
           return s
       print('That is not an operator!')
           
           
def p_calculate(number1, operator, number2):
   
   """Performs a calculation with two numbers and an operator,
   and returns the result."""
   
   if operator == '+':
       return number1 + number2
   if operator == '-':
       return number1 - number2
   if operator == '*':
       return number1 * number2
   if operator == '/':
       return number1 / number2
   raise Exception('Invalid operator!')

   
p_main()


# In[ ]:


OPERATORS = '+', '-', '*', '/'

def f_get_number():
    return int(input('Enter an integer:'))


def f_get_operator():
    return input('Enter an operator(+,-,*,/):')


def f_calculate(number1, operator, number2) :
    return number1+number2 if operator == '+'         else number1*number2 if operator == "*"        else number1-number2 if operator == '-'        else number1/number2 if operator == '/'        else None


def f_main():
    return f_calculate(
        f_get_number(),
        f_get_operator(),
        f_get_number()
        )
print('the result is :%s' % f_main())

                


# # Comprehensions

# In[ ]:


list(range(10))


# In[ ]:


for x in range(10):
    print (x)


# # MAP

# In[ ]:


items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)


# # Filter

# In[ ]:


number_list = range(-10, 10)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)


# In[ ]:


number_list = range(-10, 10)
less_than_zero = list(filter(lambda x: x > 0, number_list))
print(less_than_zero)


# In[ ]:


l = [2,3,4,5,6,8,9,10,11,12]
list(filter(lambda x: not x%2, l))


# # Reduce

# In[ ]:


from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3])
print(product)


# # List Comprehension

# In[ ]:


multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)


# In[ ]:


squared = [x**2 for x in range(10)]
print(squared)


# # Dict Comprehension

# In[ ]:


mcase = {'a': 5, 'b': 3, 'A': 7, 'Z': 6}
{v: k for k, v in mcase.items()}


# # Set Comprehension

# In[ ]:


squared = {x**2 for x in [0,1,1,2]}
print(squared)


# # In the previous set example, can you explain the output?

# the output of 0, 1, 4 is explained by the fact that a set can only have one unique output...
# 
# 

# # LAMBDA

# In[ ]:


lambda x: x*2


# In[ ]:


lambda x:x*2


# In[ ]:


(lambda x:x*2)(4)


# In[ ]:


l = [lambda x, y: x+y]


# In[ ]:


type(l[0])


# In[ ]:


leg = ((27.154167, -80.195663), (29.195168, -81.002998), 129.7748)
start= lambda x: x[0]
end  = lambda x: x[1]
dist = lambda x: x[2]
dist(leg)


# # Iter() Operation
# Examples of Iter - lists, dictionaries etc ....

# In[ ]:


iter([2,3,4])


# In[ ]:


iter({1:2, 3:4, 5:8})


# In[ ]:


## is this iterable? Try ....

iter(104)


# In[ ]:


##Lets start with user defined String class
class String(object):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return self.val


# In[ ]:


st = String('sample string')


# # Is the above string iterable? lets test it.

# # Why didn't this work?
# 

# # What's missing?

# the magic - an_iterator.iter()

# # Then, how should we make user defined type iterable?

# This can be done by extending our String class with iter constructor

# In[ ]:


class String(object):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return self.val
    def __iter__(self):
        print ("This is __iter__ method of String class")
        return iter(self.val)  #self.val is python string so iter() will return it's iterator


# In[ ]:


st = String('Sample String')


# In[ ]:


iter(st)


# # We added a iter method in our String class to make String type as iterable. That means iter(iterable) calls iterable.iter() internally.
# You could also do this using getitem

# In[ ]:


class String(object):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return self.val
    def __getitem__(self, index):
        return self.val[index]


# In[ ]:


st = String('Sample String')


# In[ ]:


iter(st)


# # We added getitem method and user defined String type becomes iterable. So iter(iterable) look for iterable.getitem() also.¶

# # Iterator
# 1)Iterator object produces values of iterable during iteration. next() or next() is applied on iterator for producing next value
# 
# 2)It raises StopIteration exception at the end of iteration
# 
# 3)iter() function return iterator object for an iterable
# 
# 4)If iter() function is applied on iterator object, it returns same object

# In[ ]:


## List as an iterator

a_list = [1,2,3]
list_iter = a_list.__iter__()

## before python 2.6 I think - list_iter.next()
list_iter.__next__()


# In[ ]:


list_iter.__next__()


# # IterTools
# itertools is a collection of utilities that make it easy to build an iterator that iterates over sequences in various common ways
# 
# http://docs.python.org/library/itertools.html
# 
# NOTE:
# 
# iterators are not only for for
# 
# They can be used with anything that expects an iterator:
# 
# sum, tuple, sorted, and list
# 
# For example.

# In[ ]:


import itertools

letters = ['a', 'b', 'c', 'd', 'e', 'f']
booleans = [1, 0, 1, 0, 0, 1]
numbers = [23, 20, 44, 32, 7, 12]
decimals = [0.1, 0.7, 0.4, 0.4, 0.5]


# # Chain

# In[ ]:


print (list(itertools.chain(letters, booleans, decimals)))


# # compress()
# compress(): given two lists a and b, return the elements of a for which the corresponding elements of b are Tru

# In[ ]:


print (list(itertools.compress(letters, booleans)))


# # Zip ()

# In[ ]:


xi= [1.47, 1.50, 1.52, 1.55, 1.57, 1.60, 1.63, 1.65]
yi= [52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93, 61.29]
zip( xi, yi )


# In[ ]:


list(zip( xi, yi ))


# In[ ]:


zip( xi, yi )


# In[ ]:


list(_)


# # We can see that the zip() function with no arguments is a generator function, but there won't be any items. This fits the requirement that the output is iterable.

# In[ ]:


zip( (1,2,3) )


# In[ ]:


list(_)

## In this case, the zip() function emitted one tuple from each input value. This too makes considerable sense.

