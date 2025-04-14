### Descriptors
They are objects that define how attributes of another class can be accessed. 
In other words, a class can delegate the management of an attribute to another class.  

The descriptor classes are based on three special methods that form the descriptor
protocol. 
 1. _set_()
 2. _get_()
 3. _delete_()

A descriptor that implements _get_() and _set_() is called a data descriptor. 
if it just implements _get_(), then it is called a non-data descriptor. 

Methods of the descriptor protocol are, in fact, called by the object's special
_getattribute_() method on every attribute lookup. whenever such a lookup is performed, 
either by using a dotted notation in the form of instance.attribute or by using the
getattr() function call, the _getattribute_() method is implicitly invoked and it looks for
an attribute in the following orders:
1. it verifies whether the attribute is a data descriptor on the class object of the instance
2. if not, it looks to see whether the attribute can be found in the __dict__ lookup of the instance object. 
3. finally, it looks to see whether the attribute is a non-data decriptor.

Descriptors, in order to work, need to be defined as a class attributes. Also, they are 
closer to methods than normal variable attributes. 

描述符是**实现特定协议的类**，该协议包括 __get__、__set__ 和 __delete__ 方法。
描述符的作用
描述符的主要作用是对类属性的访问进行细粒度的控制，适用于以下场景：

1. 验证属性值：确保赋值符合某些规则。
2. 计算属性值：动态计算属性值，而不是直接存储。
3. 延迟加载：在需要时才加载或初始化属性值。
4. 封装逻辑：将与某个属性相关的逻辑集中管理。

描述符是实现了以下方法中至少一个的类：

1. __get__(self, instance, owner)：用于访问属性。
2. __set__(self, instance, value)：用于设置属性值。
3. __delete__(self, instance)：用于删除属性。
   
其中：
instance 是使用描述符的对象实例。
owner 是使用描述符的类。
如果一个描述符实现了 __set__ 或 __delete__ 方法，则称为数据描述符；否则称为非数据描述符。

```python
class PositiveNumber:
    def __get__(self, instance, owner):
        return instance._value

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value must be positive")
        instance._value = value


class Rectangle:
    width = PositiveNumber()
    height = PositiveNumber()

    def __init__(self, width, height):
        self.width = width
        self.height = height


rect = Rectangle(10, 5)
print(rect.width, rect.height)  # 输出: 10 5
rect.width = -5  # 抛出 ValueError
```
描述符的工作原理
描述符的作用基于 Python 的属性查找机制。当访问一个属性时，Python 会按照以下顺序查找：

如果属性是一个数据描述符，优先调用描述符的 __get__ 方法。
如果实例字典中存在该属性，则返回实例字典中的值。
如果属性是一个非数据描述符，调用描述符的 __get__ 方法。
如果以上都没有找到，抛出 AttributeError。


#### 描述符的工作机制
当我们在类中定义了一个描述符（如 PositiveNumber），并将其作为类属性（如 width 和 height）绑定到类中时，
Python 的属性访问机制会发生变化。以下是关键点：

- 描述符优先级：
    - 如果一个类属性是一个数据描述符（即实现了 __set__ 方法的描述符），那么对该属性的访问和赋值操作会被描述符拦截。
    在你的例子中，PositiveNumber 是一个数据描述符，因为它实现了 __set__ 方法。
- 赋值操作的行为：
    - 当你执行 self.width = width 时，Python 会检查 width 是否是一个描述符。
如果是描述符，Python 会调用描述符的 __set__ 方法，而不是直接将值存储到实例的字典中。


### Monkey Patch 
what is monkey patch??? 
