### Data classes
Let's assume we are building a program that does some geometric computation and Vector is a class
that allows us to hold information about two-dimensional vectors.
We will display the data of the vectors on the screen and perform common mathematical operations,
such as addition, subtraction, and equality comparison.  

Things like equlity comparison, string representation, and attribute initialization will look very similar 
and repetitive for various classes focused on data. 

If you program uses many similar simple classes focused on data that do not require complex initialization, 
you'll end up writing a lot of boilerplate code just for the \__init\__(), \__repr\__(), \__eq\__()

With the dataclasses module, we can make out vector class code a lot shorter: 
```python
from dataclasses import dataclass

@dataclass
class Vector:
    x: int
    y: int
    
    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )
    
    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y
        )
```

The dataclass class decorator reads attribute annotations of the Vector class and automatically create __init__() ... methods.
the default equality comparison assumes that the two instances are equal if all their respective attribute are equal to each other.  
But that's not all.  Data classes offer many useful features.  

We've learned already about the dangers of assigning default values to class attributes in the main clas body instead of the \__init\__()
function. The dataclass module offers a useful alternative through the field() constructor.  
this construstor allows you to specify both mutable and immutable default values for data class in a sane and secure way without risking leaking 
the state between class instances. 
Static and immutable default values are provided using the field(default=value) call. 
The mutable values should always be passed by providing a type constructor using the field(default_factory=constructor) call. 
The following is an example of a data class with two attributes that have their default values assigned through the field() constructor:
```python
from dataclasses import dataclass, field

@dataclass
class DataClassWithDefaults:
    immutable: str = field(default='this is static default value')
    mutable:  list = field(default_factory=list)


```

Data classes are similar to structs in C or Go in nature. Their main purpose is to hold data and provide shortcuts for the otherwise tedious initialization
of instance attribute.  
But they should not be used as a basis for every possible custom class. if your class isnot meant to  represent the data, and/or requires cusotom or complex 
state initialization, you should rather use the default way of initialization: through the \__init__() method. 


Dataclasses 是 Python 3.7 引入的一个模块，用于简化类的定义，特别是那些主要用于存储数据的类。它的主要作用是减少样板代码（boilerplate code），使代码更加简洁、易读和易于维护。
以下是 dataclasses 的主要作用和用途：
1. 主要作用 
   2. (1) 自动生成特殊方法
   dataclasses 可以自动生成常用的特殊方法，如 __init__()、__repr__()、__eq__() 等。
   这些方法通常在定义普通类时需要手动编写，而使用 @dataclass 装饰器后，这些方法会自动生成。
   3. 减少样板代码
   ```python
      from dataclasses import dataclass
      
      @dataclass
      class Point:
          x: float
          y: float
   ```
   4. 支持类型注解。 **注意python typing module, 需要关注一下**
   5. 提供灵活的配置选项
   2. 主要用途
      3. 定义简单的数据模型
      ```python
      from dataclasses import dataclass

      @dataclass
      class User:
          name: str
          age: int
          className: str
   
   
      jimmy = User(name='Jimmy', age=12, className='class A')
      print(jimmy)
      ## output: User(name='Jimmy', age=12, className='class A')
      ```
      4. 自动生成比较方法
      ```python
      from dataclasses import dataclass
      
      @dataclass(order=True)
      class Point:
          x: float
          y: float
      
      p1 = Point(1, 2)
      p2 = Point(3, 4)
      
      print(p1 < p2)  # 输出：True
      ```
      5. 不可变对象， 如果需要生成不可变对象（属性不能修改）， 可以设置frozen=true
      ```python
      from dataclasses import dataclass

      @dataclass(frozen=True)
      class ImmutablePoint:
          x: float
          y: float
      
      point = ImmutablePoint(1, 2)
      # point.x = 3  # 抛出异常：dataclasses.FrozenInstanceError
      ```
      6. 默认值和工厂方法。 支持为字段提供默认值或动态生成默认值（通过default_factory)
      ```python
      from dataclasses import dataclass, field
      from typing import List
      
      @dataclass
      class Config:
          name: str = "default"
          values: List[int] = field(default_factory=list)
      
      config = Config()
      print(config)  # 输出：Config(name='default', values=[])

      ```
      7. 数据验证： 结合其他库（如 pydantic 或 validators），可以在初始化时对数据进行验证。