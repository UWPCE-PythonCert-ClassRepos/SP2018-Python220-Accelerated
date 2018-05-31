
# coding: utf-8

# In[1]:


def check_prime(number):
   for divisor in range(2, int(number ** 0.5) + 1):
       if number % divisor == 0:
           return False
   return True


# In[4]:


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


# In[6]:


primes = Primes(10)
print(primes)
for x in primes:
   print(x)


# ##Generator 
# 
# A generator must have yield 
# it can yield many number of times
# Yield is two way - you can input and output 
# it saves state 
# It is a better version than Iterator or regular function 

# In[8]:


def Primes(max):
    number = 1
    while number < max:
        number += 1
        if check_prime(number):
            yield number
primes = Primes(10)
print(primes)
for x in primes:
    print(x) 


# ##Generator Expressions 
# 
# similiar to a list comprehension
# 
# [x*x for x in range(10)]
# 
# A typical list looks like this 
# 
# variable = [out_exp for out_exp in input_list if out_exp == 2]
# 
# A a generator expression: 
# 

# In[10]:


sum([x*x for x in range(10)])


# There are interesting examples of generators and iterators here 0-
# 
# http://www.learningpython.com/2009/02/23/iterators-iterables-and-generators-oh-my/
# 
# https://www.youtube.com/watch?v=OSGv2VnC0go

# # Closure examples 

# In[11]:


def outerFunction(text):
    text = text ## the text on the left side is a non local variable
 
    def innerFunction():
        print(text)
 
    return innerFunction # Note we are returning function WITHOUT parenthesis
 
if __name__ == '__main__':
    myFunction = outerFunction('Hey!')
    myFunction() 


# # Non Local Vs Global 

# In[80]:


def outside():
       d = {"outside": 1}
       def inside():
           nonlocal d
           d=["inside"] = 2
           print(d)
       inside()
       print(d)

outside()
       


# In[20]:


import functools
import heapq


# In[21]:


heap = []
heapq.heappush(heap,1)
heapq.heappush(heap,2)
heapq.heappush(heap,4)
heapq.heappush(heap,6)
heapq.heappush(heap,7)
heapq.heappush(heap,9)
heapq.heappush(heap,10)
heapq.heappush(heap,12)


# In[22]:


heapq.nsmallest(4,heap)


# In[57]:


import functools
import heapq
heap =[]


# In[58]:



push = functools.partial(heapq.heappush, heap)


# In[59]:



smallest = functools.partial(heapq.nsmallest, iterable=heap)


# In[60]:


push(1)
push(3)
push(5)
push(6)
push(8)
push(11)
push(4)
push(16)
push(17)


# In[61]:


smallest(6)


# In[63]:


taco = islice('ABCDFEG',2, None)


# In[66]:


list(taco)


# In[70]:


tacos = islice('ABCDFEG',2)


# In[71]:


list(tacos)


# In[78]:


stacos = islice('ABCDFEG',2, 4)


# In[79]:


list(stacos)

