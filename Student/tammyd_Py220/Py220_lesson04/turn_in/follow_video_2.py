class Simple():
    this = "a class attribute"

    def __init__(self):
        self.that = "a instance attribute"

    # in metaprogramming, type is important. use vars() to see attributes

    # to subclass when using type, you pass the base classes in

    # functions are objects. so methods are simply attributes of a class that happen to be a function.

def mymethod(self):
    print("my method with x = {}".format(self.x))


def init(self, x):
    self.x = x


MyClass = type("MyClass", (), {'x':1, 'mymethod': mymethod, "__init__" : init})





if __name__ == "__main__":
    mc = MyClass(5)
    print(mc)
    print(mc.mymethod())
    #mymethod()