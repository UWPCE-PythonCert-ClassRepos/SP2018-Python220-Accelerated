#namespace_understanding.py

# Spent multiple days trying to understand namespace and metaprogramming and spoke to the instructor about my difficulty. 
# Submitting lesson notes to show that I went through all the material, gave my best effort and will continue to learn this concept. 

# all objects in Python have their own namespaces
# namespaces are a core part of the python langugage
# using vars returns the actual namespace, not a copy

In [3]: class C:
   ...:     a = 5
   ...:     b = 6
   ...:     def __init__(self):
   ...:         self.x = 32
   ...:         self.y = 64
   ...:         

In [4]: vars(C)
Out[4]: 
mappingproxy({'__module__': '__main__',  #vars(C) returned a mapping proxy
              'a': 5,
              'b': 6,
              '__init__': <function __main__.C.__init__(self)>,
              '__dict__': <attribute '__dict__' of 'C' objects>,
              '__weakref__': <attribute '__weakref__' of 'C' objects>,
              '__doc__': None})


In [5]: c = C()

In [6]: vars(c)
Out[6]: {'x': 32, 'y': 64}

# dir walks the class hierarchy of a class object. this includes the instance attributes, class attributes as well as dunder methods.
#vars returns the actual namespace of that value object


In [8]: local_ns = vars()

In [9]: fred
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-9-c19ecf55be45> in <module>()
----> 1 fred

NameError: name 'fred' is not defined

In [10]: local_ns['fred'] = "something"

In [11]: fred
Out[11]: 'something'

In [12]: local_ns['fred']
Out[12]: 'something'

# able to access names from the namespace dict and from the local ns in the usual way.usual
# did not use vars to access the namespace because it would change the variable all throughout


In [13]: cns = vars(C)

In [14]: cns
Out[14]: 
mappingproxy({'__module__': '__main__',
              'a': 5,
              'b': 6,
              '__init__': <function __main__.C.__init__(self)>,
              '__dict__': <attribute '__dict__' of 'C' objects>,
              '__weakref__': <attribute '__weakref__' of 'C' objects>,
              '__doc__': None})

In [15]: cns['fred'] = 'something'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-15-4ccdcea6a8dd> in <module>()
----> 1 cns['fred'] = 'something'

TypeError: 'mappingproxy' object does not support item assignment

In [16]: C.fred
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-16-2ac70b5af96e> in <module>()
----> 1 C.fred

AttributeError: type object 'C' has no attribute 'fred'

In [17]: C.fred = 'something'

In [18]: C.fred
Out[18]: 'something'

In [19]: cns['Fred']
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-19-30cf13bfc08a> in <module>()
----> 1 cns['Fred']

KeyError: 'Fred'

In [20]: cns['fFred']
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-20-d27b7d9886af> in <module>()
----> 1 cns['fFred']

KeyError: 'fFred'

In [21]: cns['fred']
Out[21]: 'something'

# if you add an attribute to a class in the usual way w/ assignment, you have updated the mapping proxy object 

