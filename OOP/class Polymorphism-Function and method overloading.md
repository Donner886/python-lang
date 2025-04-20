### Function and method overloading
A common feature of many programming languages is function and methods overloading.  It is another type of 
polymorphism. Overloading allows you to have multiple implementations of a single function by using different 
call signatures. Either a language compiler or interpreter is able to select a matching implementation 
based on the set of function call arguments provided. Function overloading is usually resolved based on:
1. FUNCTION arity: (number of parameters): Two function can share a function name if their signatures expect a 
a different number of parameters. 
2. Types of parameters: Two function definitions can share a function name if their signatures expect different
types of parameters.  

Python lacks an overloading mechanism for functions and methods other than operators overloading. if you define 
multiple functions in a single module that share the same name, the later definition will always shadow all previous
definitions.  
If there is a need to provide several function implementations that behave differently depending on the type or number 
of  arguments provided, python offers several alternatives: 
1. Using methods and/or subclassing: Instead of relying on a function to distinguish the parameter type, 
you can bind it to specific type by defining  it as a method of that type.  
2. Using argument and keyword argument unpacking: Python allows for some flexibility regarding function
signature to support a variable number of arguments via *args and **Kwargs patterns 
3. Using type checking: The isinstance() function allows us to test input arguments against specific types and base
classes to decide how to handle them.

BUT 
1. Argument and keyword argument unpacking cna make function signatures vague and hard to maintain. 
2. Very often, the most reliable and readable substitute for function overloading is python is simply
type checking.  

That can be understood as an upside rather than downside of python. Still, this technique is convenient only for a small
number of call signatures. When the number of supported types grows, it is often better to use more modular patterns. 
such patterns rely on single-dispatch functions. 


#### Single-dispatch functions
Using multiple if isinstance() clauses can quickly get out of hand, if the number of alternative function implementations is 
really large. Good design practice dictates writing small, single-purpose functions. 
One large function that branches over several types to handle input arguments is rarely a good design.  

The Python Standard Library provides a convenient alternative. The functools.singledispatch() decorator allows you to 
register multiple implementations of a function. Those implementations can take any number of arguments but implementations will
be dispatched depending on the type of the first argument. 


#### By default, we could use the f-string to denote a raw value in string format

#### From there, we can start registering different implementations for various types using @report.register() decorator.  
#### That decorator is able to read function argument type annotations to register specific type handlers.  

```python
from functools import singledispatch

@singledispatch
def report(value):
    return f'raw: {value}'

from datetime  import datetime
@report.register
def _(value:datetime):
    
    """
    :param value: 
    :return: 
    Note that we used the
    token as the actual function name. That serves two: 
    purposes. 
        First, it is a convention for names of objects that are not supposed to be used explicitly. 
        Second, if we used the report name instead, we would shadow the original function, thus losing the ability to access it and register new types.
    """
    return f'dt: {value.isoformat()}'


from numbers import Real

@report.register
def _(value:Real):
    return f'real: {value:f}'

@report.register
def _(value:complex):
    return f"complex: {value.real:f} {value.imag:f}"

"""
    Note that typing annotations arenot necessary but we've used them as an element of good practices.
    if you donot want to use typing annotations, you can specify the registered type as the register() method argument. 
"""
@report.register(complex)
def _(value):
    return f"complex: {value.real:f} {value.imag:f}"

@report.register(int)
def _(value):
    return f'int: {value}'

```


As we see, the report() function is now an entry point to a collection of registered 
functions.  Whenever it is called with an argument, it looks in the registry mapping stored im report.register.  

That means the functools.singledispatch() decorator would not be
effective as the first argument of methods is always the same type. The functools.
singledispatchmethod() decorator keeps that calling convention in mind and allows
you to register multiple type-specific implementations on methods as well. It works
by resolving the first non-self, non-cls argument:
```python

from functools import singledispatchmethod

class Example:
    @singledispatchmethod
    def method(self, argument):
        pass
    
    @method.register
    def _(self, argument: float):
        pass

```

Remember that while the single-dispatch mechanism is a form of polymorphism that
resembles function overloading, it isn't exactly the same. You cannot use it to provide
several implementations of a function on multiple argument types and the Python
Standard Library currently lacks such a multiple-dispatch utility.







