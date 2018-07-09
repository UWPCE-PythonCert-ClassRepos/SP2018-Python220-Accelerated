"""
Exploring PyPy

Code with notes

"""

# pypy is a fast, compliant alternative implementation of the Python language with several advantages and distinct features
# speed = it is a just in time compiler that is faster than python
# memory usage
# compatibility
# stackless



import math
import time

TIMES = 10000000

# take a snapshot of system clock
init = time.clock()



# run an operation
for i in range(TIMES):
    value = math.sqrt(1 + math.fabs(math.sin(i - math.cos(i))))

print("No function: %s" % (time.clock() - init))

# Factoring the math into a function

def calcMath(i):
    return math.sqrt(i + math.fabs(math.sin(i - math.cos(i))))

# take another snapshot of system clock

init = time.clock()

for i in range(TIMES):
    calue = calcMath(i)

# check the difference. This time there is a function.
#factored out this expression and put it into a fuction
print("Function: %s" % (time.clock() - init))


# run TIMES = 1000000 under python 3.5. 
# output
    # No function: 1.141732
    # Function: 1.2815550000000002

# run TIMES = 100000000 under python 3.5. 
    # 

# not yet using jit compiler. still using standard python
# output
    # No function: 111.869146
    # Function: 123.371944

# Rick changed into another environment. 
## Python 3.6.4 was slower than Python 2.7.14!

# now let's try Pypy.
# It will run on top of Python 2.7.13
# Tammys-MBP:Py220_lesson10 tammydo$ pypy jit_test.py 
# output
    # No function: 0.845679
    # Function: 0.863227

# Pypy is so much faster!












# # -------------------------------------------------------
# # Timeit tutorial
# # rriehle

# from timeit import timeit as timer

# my_repititions = 10000
# my_range = 10000
# my_lower_limit = my_range / 2

# my_list = list(range(my_range))


# def multiply_by_two(x):
#     return x * 2


# def greater_than_lower_limit(x):
#     return x > my_lower_limit


# print("\n\nmap_filter_with_functions")
# # map_filter_with_functions = map(multiply_by_two, filter(greater_than_lower_limit, my_list))
# # print(*map_filter_with_functions)
# print(timer(
#     'map_filter_with_functions = map(multiply_by_two, filter(greater_than_lower_limit, my_list))',
#     globals=globals(),
#     number=my_repititions
# ))

# print("\n\nmap_filter_with_lambdas")
# # map_filter_with_lambdas = map(lambda x: x * 2, filter(lambda x: x > my_lower_limit, my_list))
# # print(*map_filter_with_lambdas)
# print(timer(
#     'map_filter_with_lambdas = map(lambda x: x * 2, filter(lambda x: x > my_lower_limit, my_list))',
#     globals=globals(),
#     number=my_repititions
# ))

# print("\n\ncomprehension")
# # comprehension = [x * 2 for x in my_list if x > my_lower_limit]
# # print(*comprehension)
# print(timer(
#     'comprehension = [x * 2 for x in my_list if x > my_lower_limit]',
#     globals=globals(),
#     number=my_repititions
# ))

# print("\n\ncomprehension_with_functions")
# # comprehension_with_functions = [multiply_by_two(x) for x in my_list if greater_than_lower_limit(x)]
# # print(*comprehension_with_functions)
# print(timer(
#     'comprehension_with_functions = [multiply_by_two(x) for x in my_list if greater_than_lower_limit(x)]',
#     globals=globals(),
#     number=my_repititions
# ))

# print("\n\ncomprehension_with_lambdas")
# # comprehension_with_lambdas = [lambda x: x * 2 for x in my_list if lambda x: x > my_lower_limit]
# # comprehension_with_lambdas = [(lambda x: x * 2)(x) for x in my_list if (lambda x: x)(x) > my_lower_limit]
# # print(*comprehension_with_lambdas)
# print(timer(
#     'comprehension_with_lambdas = [(lambda x: x * 2)(x) for x in my_list if (lambda x: x)(x) > my_lower_limit]',
#     globals=globals(),
#     number=my_repititions
# ))


# #  Consider order of operations between the forms.
# #  In map_filter_with_functions the filter is applied before the map expression
# #  Is that true in the other variatins?