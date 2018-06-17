'''
Jay Johnson - Lesson01 - Activity01 - Iterators & Iteratables
iterator_1
'''


def frange(start, stop, step=1):
    '''match range()'''
    i = start
    while i < stop:
        yield i
        i += step

print(list(frange(2,20,2)))
print(list(range(2,20,2)))

#for i in range(2, 20, 2):
    #print(i)
