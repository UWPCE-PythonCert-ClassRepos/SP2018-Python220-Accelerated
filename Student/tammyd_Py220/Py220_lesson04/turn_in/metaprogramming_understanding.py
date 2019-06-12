#metaprogramming_understanding.py

In [22]: class Dummy:
    ...:     pass
    ...: 
    ...: 

In [23]: obj = Dummy
    ...: 

In [24]: 

In [24]: vars(obj)
Out[24]: 
mappingproxy({'__module__': '__main__',
              '__dict__': <attribute '__dict__' of 'Dummy' objects>,
              '__weakref__': <attribute '__weakref__' of 'Dummy' objects>,
              '__doc__': None})

In [25]: setattr(obj, "name", "Fred")

In [26]: vars(obj)
Out[26]: 
mappingproxy({'__module__': '__main__',
              '__dict__': <attribute '__dict__' of 'Dummy' objects>,
              '__weakref__': <attribute '__weakref__' of 'Dummy' objects>,
              '__doc__': None,
              'name': 'Fred'})

In [27]: obj.name
Out[27]: 'Fred'

In [28]: 

# can also get the value using getattr. they are exactly the same


# delattr 
In [31]: delattr(obj, "name")

In [32]: vars(obj)
Out[32]: 
mappingproxy({'__module__': '__main__',
              '__dict__': <attribute '__dict__' of 'Dummy' objects>,
              '__weakref__': <attribute '__weakref__' of 'Dummy' objects>,
              '__doc__': None})

In [33]: obj.name
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-33-8d60453bb8a2> in <module>()
----> 1 obj.name

AttributeError: type object 'Dummy' has no attribute 'name'

# what's the difference from the usual way? getattr and setattr use strings. using a string in a variable allows you to manipulate the code. no need to know the attribute up front


In [34]: att_name = "this"

In [35]: att_value = "something"

In [36]: setattr(obj, att_name, att_value)

In [37]: vars(obj)
Out[37]: 
mappingproxy({'__module__': '__main__',
              '__dict__': <attribute '__dict__' of 'Dummy' objects>,
              '__weakref__': <attribute '__weakref__' of 'Dummy' objects>,
              '__doc__': None,
              'this': 'something'})

# now we can see that "this" was set to "something" even though it was coming from variable names

# enables us to manipulate objects at runtime without knowing the names when you write the code. 

######### THIS WHAT HE MEANS WHEN HE SAYS METAPROGRAMMING. #########


