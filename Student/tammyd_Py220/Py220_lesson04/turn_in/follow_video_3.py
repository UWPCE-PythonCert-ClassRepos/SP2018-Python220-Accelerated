follow_video_3.py

# every object in python has a metaclass and the default metaclass is type. that is, type is used to create the class
# to define a metaclass, use the metaclass keyword argument

#class Foo(metaclass = MyMetaClass):
#    pass
# same as doing "class Foo(metaclass = type)"

# metaclass handy for when you need to manage the data from one or more classes


"""
Complete do-nothing metaclass example

It serves to show when each special method of the metaclass is called.

"""


class CoolMeta(type):
    # manipulate before the class is created. 
    def __new__(meta, name, bases, dct):
        print('Creating class in CoolMeta.__new__', name)
        return super().__new__(meta, name, bases, dct)

    # the actual class object created
    def __init__(cls, name, bases, dct):
        print('Initializing class  in CoolMeta.__init__', name)
        super().__init__(name, bases, dct)

    # used when the __init__ is called
    def __call__(cls, *args, **kw):
        print('calling CoolMeta to instantiate ', cls)
        return type.__call__(cls, *args, **kw)


class CoolClass(metaclass=CoolMeta):
    def __init__(self):
        print('And now my CoolClass object exists')


print('everything loaded, instantiate a CoolClass instance now')

if __name__ == "__main__":
    cc = CoolClass()






######  NAME MANGLER  ######


"""
class NameMangler(type):
    def __new__(cls, clsname, bases, _dict):
        uppercase_attr = {}
        for name, val in _dict.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()]= val
                uppercase_attr[name] = val
            else: 
                uppercase_attr[name] = val

        return super().__new__(cls, clsname, bases, uppercase_attr)

class Foo(metaclass= NameMangler):
    x = 1
    Y = 5


"""