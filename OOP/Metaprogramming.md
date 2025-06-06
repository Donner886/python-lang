### Metaprogramming

In This section, I want to know:

1. what is the metaprogramming in python?
2. how to conduct metaprogramming in  python?
3. what is the most common used usage via  metaprogramming in python?
4. other contribution in aspect of OOP

Many programmers associate it almost exclusively with programs that can inspect and manipulate their own code at source level.

Programs manipulating their own source code are definitely one of the most striking and complex examples of applied metaprogramming,

but metaprograming takes many forms and doesn't always have to be complex nor hard.

Python is expecially rich in features and modules that make certain metaprogramming techniques simple and natural.

In this chapter, we will explain what metaprogramming really is and present a few practical approaches to metaprogramming in Python. We will start with simple metaprogramming techniques like function and class decorators but will also cover advanced techniques to override

the class instance creation process and the use of metaclasses.  We will finish with examples of most powerful but also dangerous approach to  metaprogramming, which is code generation patterns.

Maybe we could find a good academic definition of metaprogramming, but this is a book that is more about good software craftsmanship than about computer science theory. this is why we will use our own informal definition of metaprogramming:

_"Metaprogramming is a technique of writing computer programs that can treat themselves as data, so they can introspect, generate, and/or modify themselves while running."_

Using this definition, we can distinguish between two major branches of metaprogramming in Python.  
1.  Introspect-oriented metaprogramming: Focused on natural introspection capabilities of the language and dynamic definitions of function and types.
2. Code-oriented metaprogramming: Metaprogramming focused on treating code as mutable data structures.  

Introspection-oriented metaprogramming concentrates on the language's ability to introspect its basic elements, such as functions, classes, or types, and to 
create or modify them on the go. Python really provides a lot of tools in this area. this feature of the python language is often used by 
Integrated Development Environments to provide real-time code analysis and name suggestions.  The easiest possible metaprogramming tools in python that utilize
language introspection features are decorators that allow for adding extra functionality to existing functions, methods, or classes.  
next are special methods of classes that allow you to interfere with the class instance creation process. the most powerful are metaclasses, which allow programmer 
to even completely redesign python's implementation of object-oriented programming.  

Code-oriented metaprogramming allows programmers to work directly with code, either in its raw(plain text) format or in the more programmatically accessible abstract syntax tree(AST) form.  

## Using decorators to modify function behavior before use
Decorators are one of the most common inspection-oriented metaprogramming techniques in Python. Because functions in python are first-class object, they can be inspected and 
modified at runtime. Decorators are special functions capable of inspecting,  modifying, or wrapping other functions.  
The decorator syntax is in fact a syntactic sugar that is supposed to make it easier to work with functions that extend exsiting code objects with additional behavior.  
A decorator usually returns a new function object that replaces the pre-existing decorated function name.  
Function decorators are often used to intercept and preprocess original function arguments, modify the return values, or enhance then function call context with additional functional 
aspects like logging, profiling,or evaluating a caller's authorization/authentication claims.  

the @lru (last recently used) cache of return values for a give function. It intercepts incoming function arguments and compare them with a list of recently used arguments sets. 
if there is a match, it returns the cached values instead of calling the decorated function.  If there is no match, the original function will be called first and the return value 
will be stored in the cache for later use.  In our example, the cache will hold no more than 100 values. 
What is really interesting is that the use of @lru_cache is already a metaprogramming technique.  It takes an existing code object and modifies its behavior. 
It also intercepts arguments and inspects their value and type to decide whether these can be cached or not.  
In most cases, decorators make code shorter, easier to read, and also cheaper to maintain. This means that they serve as a perfect introductory technique to metaprogramming.  
Other metaprogramming tools that are available in Python may be more difficult to understand and master. 

### One step deeper: class decorators
One of the lesser-known syntax features of python is class decorator.  We've already used some class decorators in previous chapters. There were the @dataclass decorator from the dataclasses
module, and @runtime_checkable from the typing module. Both decorators rely on Python's introspection capability to enhance existing classes with extra behavior: 
1. The @dataclass decorator inspects class attribute annotations to create a default implementation of the __init__() method and comparison protocol that saves developers from writing repeatable 
boilerplate code.  It also allows you to create custom "frozen" classes with immutable and hashable instances that can be used as dictioanry keys. 
2. The @runtime_checkable decorator marks protocol subclasses as "runtime checkable". It means that the argument and return value annotation of the Protocol subclass can be used to determine 
at runtime if another class implements an interface defined by the protocol class.  

The best way to understand how class decorators work is to learn by doing. 
One of the great features of dataclasses is the ability to provide a default implementation of the __repr__() method. That method returns a string representation of the object that can be displayed
in an interactive session, logs, or in stardard output.  
For custom classes, this __repr__() method will by default include only the class name and memory address, but for dataclasses it automatically includes a representation of each individual feild of 
the dataclass. 
```python
from typing import Any, Iterable

UNSET = object()

def repr_instance(instance: object, attrs: Iterable[str]) -> str:
    attr_values: dict[str, Any] = {
        attr: getattr(instance, attr, UNSET)
        for attr in attrs
    }
    sub_repr = ",".join(
        f"{attr}={repr(val) if val is not UNSET else 'UNSET'}"
        for attr, val in attr_values.items()
    )
    return f"<{instance.__class__.__qualname__}:{sub_repr}>"
```
repr() --> Python的内置函数，主要用来提供一个对象的完整，明确的字符串表示形式，语法repr(object)获取字符串表示的对象。 
__ s = "Hello, world!"
__ print(repr(s))  # 输出: 'Hello, world!'
与 str() 对比
虽然 repr() 和 str() 都能将对象转换成字符串，但它们的目的不同：
1. repr() 目标是生成一个准确的、适合开发者阅读的字符串，通常包括所有信息以便于调试。
2. str() 目标是生成一个人类可读的或友好的输出。


our repr_instance() function starts by traversing instance attributes using the getattr() function over all attribute names provided in the attrs arguments. 
It's good so far but we need to pass the object instance explicitly and know all the possible attribute names before we want to print them.  That's not very 
convenient because we will have to update the arguments of repr_instance() every time the structure of the class changes.  
we will write a class decorator that will be able to take the repr_instance() function and inject it into a decordated class. We will also use class attribute
annotations stored under a class's __annotations__ attribute to determine what attributes we want to include in representation. 

```python
def autorepr(cls):
    attrs = set.union(
        *(
            set(c.__annotations__.keys())
            for c in cls.mro()
            if hasattr(c, "__annotations__")
        )
    )

    def __repr__(self):
        return repr_instance(self,sorted(attrs))
    cls.__repr__ = __repr__
    return cls
```

在 @autorerepr 装饰器中定义的 __repr__ 方法是一个实例方法，这意味着它会在你用该装饰器修饰的类（在这个例子中是 MyClass）创建的对象上调用。当你在这个上下文中看到 self 参数时，它代表了将来使用这个类创建的任何实例。


In those few lines, we use a lot of things we learned about in Chapter4. We start by obtaining a list of annotated attributes from the cls.\__annotations\__ dictionary from each class in the class MRO. 
We have to traverse the whole MRO because annotations are not inherited from based classes. 
在python中， \__annotations\__是一个特殊的类属性，用户储存类型注解（Type annotations）。 它主要用来记录类，方法或函数的参数的返回值的类提示（Type Hints), 但不会影响运行时的行为。
它是一个字典，用来保存变量， 函数参数或返回值的类型提示。 仅仅用于静态类型检查，或者IDE提示。 
适用于类、函数、模块：
1. 在类中：存储类属性的类型注解。
2. 在函数/方法中：存储参数和返回值的类型注解。
3. 在模块中：存储模块级别的变量类型注解。

Later, we use a closure to define an inner \__repr()\__ function that has access to the attrs variable from the outer scope.  when that's done, we override the existing cls.\__repr\__() method with a new implementation. 
We can do that because function objects are already non-data descriptors. It means that in the class context they become methods and simply receive an instance object as a first argument.
1. 函数对象（Function Objects)： python中，函数是一等对象（first-class objects)， 可以像普通变量一样传递。  
```python
def greet(name):
    return f"hello, {name}"
print(type(greet))
```
2. 描述符（ Descriptor) 是实现了\__get\__(), \__set\__(), \__delete\__()方法的对象。
   1. 数据描述符(Data descriptor): 实现了 \__set\__ 或者 \__delete\__方法
   2. 非数据描述符 （Non-data descriptor):  仅实现了 \__get\__方法

函数是典型的非数据描述符。 因为函数中实现了 \__get\__()。 
这句话讨论的是Python中函数对象作为非数据描述符的特性， 以及他们如何在类（context)中自动转化为绑定（bound methods)。具体来说这是关于python如何处理类中的方法定义及其调用机制的
一个核心概念
1. 在类外部定义的函数： 如果你只是简单地在一个模块的作用域内定义一个函数，那么它就是一个普通的函数对象。 它不会自动实现非数据描述符的协议。也不会通过.method的方式绑定到任何实例上。 
2. 在类内部定义的函数： 当你在类中定义一个函数（通常称为方法）时，这个函数实际上是一个非数据描述符。当你通过类的一个实例访问这个方法时，Python的特殊方法查找机制会调用这个函数对象的 __get__() 方法，
返回一个绑定方法，这个方法会在调用时自动传入实例本身作为第一个参数。
```python

class MyClass:
    def my_method(self):
        print(f"Called with {self}")

# 创建类的实例
obj = MyClass()

# 访问my_method属性
bound_method = obj.my_method  # 这里触发了my_method的__get__()方法

# 调用绑定的方法
bound_method()  # 输出: Called with <__main__.MyClass object at ...>

##########################################################
def standalone_function(self):
    print(f"Called with {self}")

# 检查standalone_function是否有__get__方法
print(hasattr(standalone_function, '__get__'))  # 输出: True

# 手动调用__get__方法
bound_method = standalone_function.__get__(None, object)  # 不绑定到任何实例
print(bound_method)  # 输出: <function standalone_function at ...>

bound_method = standalone_function.__get__(obj, MyClass)  # 绑定到实例
print(bound_method)  # 输出: <bound method standalone_function of <__main__.MyClass object at ...>>
bound_method()  # 输出: Called with <__main__.MyClass object at ...>

```

Modifying existing classes in place(also known as monkey patching) is a common technique used in class decorators. the other  way to enhance existing with decorators is through utilizing 
closures to create new subclasses on the fly.  If we had to rewrite our example as a subclassing pattern, we could write it as follows: 
```python
def autorepr2(cls):
    attrs = cls.__annotations__.keys()
    class Klass(cls):
        def __repr__(self):
            return repr_instance(self, attrs)
        
    return Klass

```
**The major drawback of using closures  class decorators this way is that this technique affects class hierarchy. Among others, this will override the class's \__name\__, \__qualname\__, and \__doc\__
attributes. This makes the use of subclassing in class decorator limited.** 

### Mixin 
Still, despite this single caveat, class decorators are a simple and lightweight alternative to the popular mixin class pattern.  A mixin in pattern is a class the is not meant to be instantiated but is 
instead used to provide some reusable API or functionality to other existing class. Mixin classes are almost always added using multiple inheritance. 
Mixin classes form a useful design pattern that is utilized in many libraries and frameworks. To name one, Django is an example framework that uses them extensively. 
While useful and popular, mixin classes can cause some trouble if not designed well, because, in most cases, they are require the developer to rely on multiple inheritance. 
As we start earlier, Python handles multiple inheritance relatively well, thanks to its clear MRO implementation. 
Anyway, try to avoid subclassing multiple classes if you can, as multiple inheritance makes code complex and hard to work with.  This is why class decorators may be a good replacement for mixin classes.

In general, decorators concentrate on modifying the behavior of functions and classes before they are actually used. 
Function decorators replace existing functions with their wrapped alternatives.
Class decorators , usually modifying the class definition.   But there are some metaprogramming techniques that concentrate more on modifying code behavior when it is actually in use.  
One of those techniques relies on intercepting the class instance creation process through the overriding of the \__new\__ method. 





















