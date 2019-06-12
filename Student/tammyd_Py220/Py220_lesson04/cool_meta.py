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
