### Class instance initialization

What makes python different from other statically typed OOP programming languages
is its approach to object attribute declaration and initialization.  
In short, Python classes does not require you to define attributes in the class body.
A variable comes into existence at the time when it is initialized. 
that's why the canonical way to declare object attributes is through assigning their
values during object initialization in the __init__() method.  
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```
```python
class Point:
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
```
The above code is a classic example of a foreign language idiom replicated in Python
Most of all, it is redundant. class attribute values will always be shadowed by object
attributes upon initialization. But it is also a dangerous code smell. 
it can lead to problematic errors if one decides to assign as a class attribute a mutable
type like list or dict

**Lesson learned from above code**

    When accessing an attribute with self.attribute, python will first look up the same name 
    in class instance namespace. if that lookup fails, it will perform a lookup in the class type
    namespace
    When assigning values through self.attribute from within the class method, the behavior is 
    completely different: new values are always assigned in the class instance namespace.  
       

### Attibute access pattern
Name mangling (名称改编)： Every time an attribute is prefixed by __ (two underscores) within a python 
class body, it is renamed by the interpreter in the fly: 
```python
class MyClass:
    def __init__(self):
        self.__secret_value = 12
```
Accessing the __secret_value attribute by its initial name outside of class will raise an AttributeError. 
具体来说，当定义一个类时，如果你使用两个下划线开头但没有以两个下划线结尾的名称（例如 __method_name），
Python 会自动将这个名称进行改编，添加一个前缀 _ClassName，其中 ClassName 是该类的名字。这样做的目的是为了保护这些名称不与子类中的相同名称相冲突。
```python
class MyClass:
    def __init__(self):
        self.__var = 10

obj = MyClass()
# 下面这行会抛出 AttributeError
# print(obj.__var)

# 但是你可以通过这种方式访问：
print(obj._MyClass__var)
```
Still, it is not recommended to use name mangling in base classes by default, 
just to avoid any collisions in advance. 

