
# coding: utf-8

# In[6]:


## Null wrapper decorators
def null_decorator(funct):
    funct


# In[8]:


@null_decorator
def greet():
   return 'Hello!'


# In[9]:


class my_decorator(object):
    
    def __init__(self, f):
        print()


# In[11]:


## Context managers


# Think of them like cleaners use with statement to bind all your relevant commands. They close connections that are open when you are done. The moment you have a with, it handles the closing of the connection, the cashing, etc.
# 
# There are two methods to benefit from context manager functionality:
# __enter__() and __exit__()

# In[12]:


## Recursions
## need a base case and a recursion case


# In[14]:


## >>> from factorial import factorial
## >>> factorial(4)

def factorial(n):
	if n==1:
	   return 1
	return n*factorial(n-1)


# In[15]:


factorial(3)


# In[16]:


factorial(10)


# In[17]:


factorial(10) / factorial(9)


# Many people are familiar with recursion but not backtracking.
# Backtracking is when you have a node with multiple options which in turn have multiple options (a tree like structure) and you are trying all options until you find a path with the shortest length.

# In[18]:


def permute(list, s):
    if list == 1:
        return s
    else:
        return [ y + x
                 for y in permute(1, s)
                 for x in permute(list - 1, s)
                 ]


# In[21]:


permute(3, ['1','2','5'])

