#!/usr/bin/env python3

'''
create a new metaclass that combines the Singleton and Mangler classes

“The singleton pattern is a software design pattern that restricts the
instantiation of a class to one object.”

'''


class MangledSinglton(type):
    instance = None

    # this is the code that creates custom attributes for the new class
    def __new__(cls, clsname, bases, _dict):
        uppercase_attr = {}
        for name, val in _dict.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
                uppercase_attr[name.upper()*2] = val
                uppercase_attr[name.lower()] = val
                uppercase_attr[name.lower()*2] = val
            else:
                uppercase_attr[name] = val
        return super().__new__(cls, clsname, bases, uppercase_attr)

    # this is the Singleton code which restricts the instantiation of a class
    # to one object
    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance




class MyClass(metaclass=MangledSinglton):
    x = 1

o1 = MyClass()
o2 = MyClass()
print(o1.X)
assert id(o1) == id(o2)
print(bool(id(o1) == id(o2)))
