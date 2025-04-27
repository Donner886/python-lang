### Interfaces, Patterns, and Modularity
In this chapter, we will dive deep into the realm of design patterns through the lens of interaces, patterns, and modularity.  
We've already neared this realm when introducing the concept of programming idioms.  Idioms can be understood as small 
and well-recognized programming patterns for solving small problems.  
The key characteristic of a programming idiom is that it is specific to a single programming language. 
While idioms can often be ported to a different language, it is not guaranteed that the resulting code will feel natural 
to "native" users of that programming language. 

1, Idioms generally are concerned with small programming constructs - usually a few lines of code.  
2, Design patterns, deal with much larger code structures-functions and classes. they are also definitely more ubiquitous.
Design patterns are reusable solutions to many common design problems appearing in software engineering. 

In this chapter, we will look at a quite unusual take on the topic of design patterns.  
Many programming books start by going back to the unofficial origin of software design patterns. 
the [ Design Patterns: Elements of Reusable Object-Oriented Software book by Gamma, Vlissides, Helm, and Johnson. 
What usually follows is a lengthy catalog of classic design patterns with more or less idiomatic examples of their
python implementation.  Singletons, Factories, adapters, flyweights, bridges, visitors, strategies, and so on and so forth. 

Instead, we will focus on two key "design pattern enablers"
1. Interfaces
2. Inversion of control and dependency injectors.

These two concepts are "enablers" because without them we wouldn't have proper language terms to talk about design patterns.  
By discussing the topic of interfaces and inversion of control, we will be able to better understand what the challenges are 
for building modular applications.


### Interfaces
Broadly speaking, an interface is an intermediary that takes part in the interaction between two entities.
In programming, interface may mean two things:
1. the overall shape of the interaction plane that code can have 
2. the abstract definition of possible interactions with the code that is intentionally separated from its implementation.  
In the spirit of the first meaning, the interface is a specific conbination of symbols used to interact with the unit of code.
the interface of a function, for instance, will be the name of that function, its input arguments, and the output it returns.
the interface of a object will be all of its methods that can be invoked and all the attributes that can be accessed.

Collections of units of code(functions, object, classes) are often grouped into libraries. In python, libraries take
the form of modules and packages(collections of modules). They also have interfaces. Contents of modules and packages usually 
can be used in various combinations and you don't have to interact with all of their contents. 

In a purist approach, the definition of interface does not provide any usable implementation of methods.  It just defines an
explicit contract for any class that wishes to implement the interface.   Interface are often composable. This means that a 
single class can implement multiple interfaces at once. In this way, interfaces are the key building block of design patterns.
A single design pattern can be understood as a composition of specific interfaces.Similar to interfaces, design patterns 
do not have an inherent implementation. they are just reusable scaffolding for developers to solve common problems.  

Python developers prefer duck typing over explicit interface definitions but having well-defined interaction contracts between
classes can often improve the overall quality of the software  and reduce the area of potential errors. 
For instance, creators of a new instance implementation get a clear list of methods and attributes that a given class needs to 
expose. 

**Typing在编程领域中， 指的是类型系统**

Duck Typing（鸭子类型） 是动态编程语言中的一种编程风格，尤其在 Python 中被广泛采用。这个术语来源于一句格言：“如果它走起来像鸭子，叫起来像鸭子，
那么它就是一只鸭子。” 这句话的意思是，在鸭子类型中，对象的类型或类不是决定性的；重要的是对象是否具有执行特定操作所需的方法和属性。
在鸭子类型中，不需要显式地检查对象是否属于某个特定类型或实现某个接口。相反，你只需关注对象是否支持你想要调用的方法或属性。
这种做法提高了代码的灵活性和可扩展性，因为它允许使用不同类型的对象，只要它们满足某些行为要求即可。

Python has a completely different typing philosophy than these languages, so it does not have native support for interfaces
verified at compile time.  Anyway, if you would like to have more explicit control of application interfaces, there is a handful
of solutions to choose from: 
1. Using a third-party framework like zope.interface that adds a notion of interfaces.
2. Using Abstract Base Classes (ABCs)
3. Leveraging typing annotation,


#### zope.interface
There are a few frameworks that allow you to build explicit interfaces in Python. The most notable one is a part of the 
ZOPE project. It is the zope.interface package.  Although, nowadays, Zope is not as popular as it used to be a decade ago.
the zope.interface package is still one of the main components of the still popular Twisted framework. It predated mainstream
python features ABCs so we will start from it and later see how it compares to other interface solutions. 

The interface concept works best for areas where a single abstraction can have multiple implementations or can be applied to 
different objects that probably should not be tangled with inheritance structure.  

itertools.combinations(iterable,r ): Return r length subsequences of elements from the input iterable.  
The output is a subsequence of product() keeping only entries that are subsequences of the iterable. the length of the output 
is given by math.com() which computes n!/r!/(n-r)! when r<=  n or zero when r>n
The combination tuples are emitted in lexicographic order according to the order of the input iterable. if the input iterable
is sorted, the output tuples will be produced is sorted order. 
Elements are treated as unique based on the position, not on their value. if the input elements are uniquem there will be no
repeated values within each combination.  

The common convention for Zope is to prefix interface class with I. The Attribute constructor denotes the desired attribute 
of the objects implementing the interface. Any method defined in the interface class will be used as an interface method 
declaration.  Those methods should be empty. the common convention is to use only the docstring of the method body. 

When you have such an interface defined, you must denote which of your concrete classes implement that interface.  
this style of interface implementation is called explict interfaces and is similar in nature to traits in Java. 
In order to denote the implementation of a specific interface. you need to use the implementer() class decorator.  

It is common to say that the interface defines a contract that a concrete implementation needs to fulfil. 
the main benefit of  this design pattern is being able to verify consistency between contract and implementation before 
the object is used. With the ordinary duck-type approach,  you only find inconsistencies when there is a missing attribute 
or method at runtime.  

With zope.interface, you can introspect the actual implementation using two methods from zope.interface.verify module to find 
inconsistency early on: 
1. verifyClass(interface, class_object): This verifies the class object for the existence of methods and correctness of their
signatures without looking for attributes. 
2. verifyObject(interface, instance): This verifies the methods, their signatures, and also attributes of the actual object instace.

### Using function annotations and abstract base classes



