#### Using function annotations and abstract base classes
Formal interface are meant to enable loose coupling in large application, and not to provide you with more layers of complexity.  
zope.interface is a great concept and may greatly fit some projects, but it is not a silver bullet. By using it, you may 
shortly find yourself spending more time on fixing issues with incompatible interfaces for third-party classes and providing
never-ending layers of adapters instead of writing the actual implementation.  
If you feel that way, then this is a sign that something went wrong. Fortunately, python supports building a lightweight 
alternative to the explicit interfaces.  It's not a full-fledged solution such as zope.interface or its alternatives but 
generally provides more flexible applications.  you may need to write a bit more code, but in the end, you will have something 
that is more extensible, better handles external types, and maybe more future-proof. 

** Note that python, at its core, does not have an explicit notion of interfaces, and probably never will have, but it has some 
of the features that allow building something that resembles the functionality of interfaces. **
the features are as follows: 
1. ABCs
2. Function annotations
3. Type annotations

As you probably know, direct type comparison is considered harmful and not pythonic.   You should always avoid comparisons as in the 
following example: 
```python
assert  type(instance) == list
```
Comparing types in functions or methods this way completely breaks the ability to pass a class subtype as an argument to the 
function. ** Slightly better approach is to use the isinstance() function, which will take the inheritance into account:
```python
assert isinstance(instance, str)
```
The additional advantage of isintance() is that you can use a larger range of types to check the type compatibility. For instance, 
if your function expects to receive some sort of sequence as the argument, you can compare it against the list of basic types:
```python
assert isinstance(instance, (list, tuple, range))
```
And Such type compatibility checking is OK in some situations but is still not perfect.  
It will work with any subclass of list, tuple, or range, but will fail if the user passes something that behaves exactly 
the same as one of these sequence types but does not inherit from any of them. For instance, let's relax our requirements 
and say that you want to accept any kind of iterable as an argument. what would you do? 

The list of basic types that are iterable is actually pretty long. You need to cover list, tuple, range, str, bytes, dict,
set, generators, and a lot more.  The list of applicable built-in types is long, and even if you cover all of them, it will 
still not allow checking against the custom class that defines the __iter__() method but inherits directly from object. 

And this is the kind of situation where ABCs are the proper solution.  ABC is a class that does not need to provide a concrete 
implementation, but instead defines a blueprint of a class that may be used to against type compatibility. This concept is 
very similar to the concept of abstract classes and virtual methods known in the C++ language. 

Abstract base classes are used for two purposes:
1.  Checking for implementation completeness
2. Checking for implicit interface compatibility

The usage of ABCs is quite simple. you start by defining a new class that either inherits from the abc.ABC base class or havs
abc.ABCMeta as its metaclass.  We won't be discussing metaclasses until Chapter 8, Element of Metaprogramming.

The following is an example of a basic abstract class that defines an interface that doesn't do anything particularly special:
```python
from abc import ABC, abstractmethod
class DummyInterface(ABC):
    
    @abstractmethod
    def dummy_method(self):
        pass
    
    @property
    @abstractmethod
    def dummy_property(self):
        pass
```
The @abstractmethod decorator denotes a part of the interface that must be implemented (by overriding) in classes that will 
subclass out ABC. if a class will have a nonoverriden method or property, you won't be able to instantiate it. Any attempt 
to do so will result in a TypeError exception. 

This approach is a greate way to ensure implementation completeness and is as explicit as zope.interface alternative. 
if we would like to use ABCs instead of zope.interface in the example from the previous section, we could do the following 
modification of class definitions. 
```python
from abc import ABC, abstractmethod
from dataclasses import dataclass

class ColliderABC(ABC):
    @property
    @abstractmethod
    def bounding_box(self):
        pass
    
@dataclass
class Square(ColliderABC):
    x: int
    y: int
    width: int
    
        
@dataclass
class Rectangle(ColliderABC):
    x: int 
    y: int 
    width: int
    length: int
    
    
@dataclass
class Circle(ColliderABC):
    x: int
    y: int 
    radius: int
```

We had to use subclassing（子类化） so coupling between components is a bit more tight but still comparable to that of zope.interface. 
As far as we rely on interfaces and not on concrete implementations, coupling is still considered loose.  
But things could be more flexible. This is python and we have full introspection power. Duck typing in pythons allows us to use 
any that "quacks like a duck" as if it was a duck.Unfortunately, usually it is in the spirit of "try and see". We assume 
that the object in the given context matches the expected interface. And the whole purpose of formal interface was to actually 
have a contract that we can validate against.  Is there a way to check whether an object matches the interface without actually 
trying to use it first.  
