### Dynamic Polymorphism
Polymorphism is a mechanism found commonly in OOP language. Polymophism 
abstracts the interface of an object from its type. 

if it walks like a duck and it quacks like a duck, then it must be a duck
如果它走路像鸭子，叫声也像鸭子，那么它必定是只鸭子。

这句话实际上反映了编程中的“鸭子类型”（Duck Typing）概念：在动态类型语言中，
如Python，判断一个对象是否属于某种类型不是依据其实际类型，
而是依据其是否具有执行特定任务所需的方法和属性。
这一原则强调的是对象的行为而非其所属的具体类型。

Application of that principle in python means that any object can be used 
within a given context as long as the object works and behaves as the context
expects.  
Because python does not enforce types or interfaces of function arguments, it doesnot 
matter what types of objects are provided to the function. what matters instead is 
which method of those objects are actually used within the function body.

The approach to polymorphism and typing is really powerful and flexible,
although it has some downsides.  Due to the lack of type and interface enforcement, 
it is harder to verify the code's correctness before execution. That's why high-quality
applications must rely on extensive code testing with rigorous coverage of every path 
that code execution can take.  Python allows you to partially overcome this problem 
through type hinting annotations that can be verified with additional tools before runtime. 

The dynamic type system of Python together with the duck-typing principle creates
an implicit and omnipresent form of dynamic polymorphism that makes python very similar to 
Javascript, which also lacks static type enforcement.  but there are other forms of polymorphism
available to python developers that are more "classical" and explicit in nature.  One of those forms 
is operator overloading.  

#### Operators overloading
The semantics and implementation of all Python operators are already different 
depending on the types of operands. Python provides multiple built-in types together with 
various implementation of their operators, but it doesnot mean that 
every operator can be used with any type. 

Operation overloading is just the extension of the built-in polymorphism of operators
already included in the programming language. Many programming languages, 
including python, allow you to define a new implementation for operand
types that didnot have a valid operator implementation or shadow existing 
implementation through subclassing. 

#### Dunder methods(language protocols)
Dunder 是首位有两条下划线的特殊方法和属性的简介读法
The python data model specifies a lot of specially named methods that 
can be overridden in your custom classes to provide them with additional 
syntax capabilities. 
You can recognize these methods by their specific naming conventions that wrap
the method name with double underscores.  Because of this, they are sometimes
referred to as dunder methods. It is simply shorthand for double underscores. 

The most common and obvious example of such dunder methods is \__init\__()".

```python
class Demo:
    def __init__(self, name):
        self.name = name

```
These method, either alone or when define in a specific combination, 
constitute the so-called language protocols. 
If we say that an object implements a specific language protocol, it 
means that it is compatible with a specific part of the Python language
syntax.

| Protocol name       | Methods                               | Description                                                                                                                                                      |  
|---------------------|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Callable protocol   | \__call\__()                          | Allow objects to be called with parentheses: <br/>  instance()                                                                                                   | 
| Descriptor protocol | \__get\__(), \__set\__(), \__del\__() | Allow us to manipulate the attribute access pattern of classes                                                                                                   | 
| Container protocol  | \__contains__()                       | Allows us to test whether or not an object contains some value<br/> using the in keyword                                                                         | 
| Iterable protocol   | \__iter__()                           | Allow objects to be iterated using the FOR keyword: <br/> for value in instace                                                                                   | 
| Sequence protocol   | \__getitem__(), __len__()             | Allow objects to be indexed with square bracket syntax and queried for length using a built-in function<br/> item = instance[index] <br/> length = len(instance) | 

**Each operator available in Python has its own protocol and operator overloading happens by implementing the dunder methods of that protocol.**  
Python provides over 50 overloadable operators that can be divided into five main groups:
1. Arithmetic operators
2. In-place assignment operators
3. Comparison operators
4. Identity operators
5. Bitwise operators

A full list of available dunder methods can be found in the Data model section of the offfcial Python documentation available at 
https://docs.python.org/3/reference/datamodel.html.

All operators are also exposed as ordinary functions in the 
operators module. The documentation of that module gives a 
good overview of Python operators. It can be found at https://docs.python.org/3.9/library/operator.html.















