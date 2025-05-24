### Interface in Python

After having went through the chapter of Interface, We can roughly summarize the content as follows: this chapter introduce
libraries related to implement interface in python:

1. Abstract Base Classes (ABCs)
2. Typing annotation
3. Inversion of Control in Application / Function

We will deep dive into those three definition above to dig out what can be used in practise, then we want to continue clear
concept that "How Interface can implement different Design Pattern"

在Python中， 接口的概念并像其他一些编程语言那样的直接和严格。 然而， Python提供了多种方式来实现类似的接口的功能， 确保类遵循特定的结构或提供某些方法。

### ABCs

This module provides the infrastructure for defining abstracts base classes(ABCs) in python, as outlines in PEP3119.
see the PEP for why this was added to Python.
The collections module has some concrete classes that derive from ABCs. these can, of course, be further derived.
In addition, the collections.abc submodule has some ABCs that can be used to test whether a class or instance provides a
particular interface, for example, if it is hashable or if it is a mapping.
This module provide the metaclass ABCMeta for defining ABCs and a helper class ABC to alternetively define ABCs through
inheritance.

### Class abc.ABCMeta

Metaclass for defining Abstract Base Classes(ABCs)
Use this metaclass to create an ABC.  An ABC can be subclassed directly, and then acts as a mix-in class.
You can also register an unrelated concrete class and unrelated ABCs as "virtual subclasses" - these and their descendants
will be considered subclass of the registering ABC by the issubclass() function, but the registering ABC won't show up in the
MRO nor will method implementations defined by the registering ABC be callable (not even via super()).
虚拟子类是指在一个基类（也称为超类）的基础上创建的一个新的类，这个新类继承了基类的所有属性和方法，并且可以添加自己的属性和方法。
这样做的好处是可以避免重复编写相同的代码，同时也可以方便地扩展和修改程序的行为。
Note that the type of ABC is still ABCMeta， therefore inheriting from ABC requires the usual precautions regarding metaclass
usage, as multiple inheritance may lead to metaclass conflicts. One may also define an abstract base class by passing the
metaclass keyword and using ABCMeta directly

```python
from abc import  ABCMeta

class MyABC(metaclass=ABCMeta):
    pass
```

__subclasshook__(subclass)
(Must be defined as a class method)
Check whether subclass is considered a subclass of this ABC. This means that you can customize the behavior of  issubclass()
further without the need to call register() on every class you want to consider a subclass of the ABC.
This method should return True, False or NotImplemented. If it returns True, the subclass is considered a subclass of this ABC.
if it returns False, the subclass is not considered a subclass of this ABC, even if it would normally be one. if it returns
NotImplemented, the subclass check is continued with the usual mechanism.

register(subclass)
register subclass as a "virtual subclass" of this ABC

### The abc Module: an ABC Support Framework

the new standard library module abc, written in pure Python, serves as an ABC support framework. It defines a metaclass ABCMeta and decorators @abstractmethod and @abstractproperty.

The ABCMeta class overrides _ _instancecheck_ _ and _ _subclasscheck_ _ and defines a register methods.  isinstance(x, B) is equivalent to issubclass(x._ _class_ _, B) or issubclass(type(x), B). (It is possible type(x) and x._ _class_ _ are not the same object, e.g. when x is a proxy object. )

These methods are intented to be called on classes whose metaclass is (derived from) ABCMeta.

The abc module also defines a new decorator, @abstractmethod, to be used to declare abstract methods. A class containing at least one method declared with this decorator 
that hasn't been overriden yet cannot be instantiated. Such methods may be called from the overriding method in the subclass(using super or direct invocation). 
__NOTE__: The abstractmethod declaration should only be used inside a class body, and only for classes whose metaclass is (derived from) ABCMeta. Dynamically adding abstract methods to a 
class, or attempting to modify the abstraction status of a method or class once it is created, are not supported. the @abstractmethod only affects subclasses derived using regular inheritance;
"virtual subclasses" registered with register() are not affected. 

__Implementation__:  The abstractmethod decorator sets the function attribute _ _isabstractmethod_ _ to the  value true. 
The ABCMeta.__new__ method computes the type attribute \__abstractmethods\__ as the set of all method names that have an \_isabstractmethod\__ attribute whose 
value is true. It does this by combining the \_abstractmethods\__ of the base classes, adding the names of all methods in the new class dict that have a true 
\__abstractmethod\__ attribute, and removing the names of all methods in new class dict that don't have a true \__isabstractmethod\__ attribute.  if the resulting 
 \__abstractmethod\__ set is non-empty, the class is considered abstract, and attempts to instantiate it will raise Typeerrpr.  

Abstract methods as defined here may have an implementation. This implementation can be called via super mechanism from the class that overrides it.
This could be useful as an end-point for a super-call in framework using cooperative multiple-inheritance. 

A second decorator, @abstractproperty, is defined in order to define abstract data attribute. Its implementation is a subclass of the built-in property class
that adds an \__isabstractmethod__ attribute. 

### ABCs for Collections and Iterators
The collections module will define ABCs necessary and sufficient to work with sets, mapping, sequences, and some helper types such as iterators and dictionary views.
All ABCs have the above-mentioned ABCMeta as their metaclass.  

The collections module has some concrete classes that derive from ABCs; these can, of course, be further derived.  In addition, 
the collection.abc submodule has some ABCs that can be used to test whether a class or instance provides a particular interface, 