# Lesson02 Activity
# .ipynb file converted to .py file


# coding: utf-8

# In[51]:


class Primes:
    def __init__(self, max):
        self.max = max
        self.number = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.number += 1
        if self.number >= self.max:
            raise StopIteration
        elif check_prime(self.number):
            return self.number
        else:
            return self.__next__()


# In[52]:


def check_prime(number):
   for divisor in range(2, int(number ** 0.5) + 1):
       if number % divisor == 0:
           return False
   return True


# In[53]:


primes = Primes(100)
print(primes)
for x in primes:
    print(x)

## Generator Intro

A generator must have a yield
It can yield many number of times
Yield is two way - you can input and output
It saves state
It is a better version than Iterator or regulat function
# In[54]:


## Generator Expressions

sum([x*x for x in range(10)])


# In[55]:


# variable = [out_exp for out_exp in input_list if out_exp == 2]


# In[56]:


def Primes(max):
    number = 1
    while number < max:
        number += 1
        if check_prime(number):
            yield number
            
primes = Primes(100)
print(primes)
for x in primes:
    print(x)


# In[57]:


## Non local vs Global


# In[58]:


def outerFunction(text):
    text = text
    
    def innerFunction():
        print("Inner:", text)
        
    return innerFunction # Note we are returning function WITHOUT parenthesis
 
if __name__ == '__main__':
    myFunction = outerFunction('Hey!')
    myFunction()


# In[59]:


def outside():
    d = {"outside": 1}
    def inside():
        d["inside"] = 2
        print(d)
    inside()
    print(d)
 
outside()


# In[60]:


def outside():
        d = {"outside": 1}
        def inside():
            #nonlocal d
            d = {"inside":2}
            print(d)
        inside()
        print("Outside")
        print(d)
 
outside()


# In[61]:


# HeapQ Code Example 0-

import heapq


# In[62]:


heap =[]
heapq.heappush(heap,1)
heapq.heappush(heap,2)
heapq.heappush(heap,4)
heapq.heappush(heap,6)
heapq.heappush(heap,7)
heapq.heappush(heap,9)
heapq.heappush(heap,10)
heapq.heappush(heap,12) 
heapq.nsmallest(4, heap)


# In[63]:


# With Partial code


# In[64]:


import functools
import heapq
heap =[]
push = functools.partial(heapq.heappush, heap)
smallest = functools.partial(heapq.nsmallest, iterable=heap)
push(1)
push(3)
push(5)
push(6)
push(8)
push(11)
push(4)
push(16)
push(17)
smallest(10)


# In[65]:


heap = []
heapq.heappush(heap,1)
heapq.heappush(heap,2)
heapq.heappush(heap,4)
heapq.heappush(heap,6)
heapq.heappush(heap,7)
heapq.heappush(heap,9)
heapq.heappush(heap,10)
heapq.heappush(heap,12) 
heapq.nsmallest(8, heap)


# In[66]:


# see if you can get izip to work ....


# In[75]:


print(*zip(heap, Primes(13)))
    


# In[29]:


from itertools import islice

slice = islice("ABCDEGF", 2, None)


# In[16]:


for x in slice:
    print(x)

