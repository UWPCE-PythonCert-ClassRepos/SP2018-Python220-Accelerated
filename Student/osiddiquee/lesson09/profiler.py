
import time

###################################################
#                                                 #
#   Decorators for profiling are located below    #
#                                                 #
###################################################

# timer decorator to test sequency functions
def timer(timed_sequence):
    def timed(index):
        start = time.time()
        result = timed_sequence(index)
        end = time.time()
        print(end - start)
        return result
    return timed

class Cache_sequence():
    def __init__(self, sequence_function):
        self.sequence_function = sequence_function
        self.cache = {}

    def __call__(self, index):
        if not index in self.cache:
            self.cache[index] = self.sequence_function(index)
        return self.cache[index]

###############################################################
#                                                             #
#   This is the definition of an arbitrary number function    #
#    In this case, it is fibonacii                            #
#                                                             #
###############################################################


#uncached version for the closure
#@timer
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)


#@timer
@Cache_sequence
def Fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

##############################
#                            #
#    Executing functions     #
#                            #
##############################

@timer
def run_functions(function):
    function(25)


print('Cached sequence function...')
run_functions(Fib)

print('Uncached sequence function...')
run_functions(F)

s = time.time()
Fib(50)
e = time.time()
print(e - s)

s = time.time()
F(50)
e = time.time()
print(e - s)








'''
    Failed attempt to make a closure to cached
'''
# making a cache with a closure
# @timer
# def number_sequence_cache(sequence_function):
#     cached = {}
#     def cache(index):
#         if index not in cache:
#             cached[index] = sequence_function(index)
#             return cache[index]
#         else:
#             return cache[index]
#     return cache
