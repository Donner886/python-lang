### Properties

Let's imagine that you have a class for user account that, among others, stores 
user's password. If you would like to emit audit logs whenever a password is 
accessed, you could either make sure that every place in your code that accesses 
user password has proper audit logs calls or proxy all access to password entry 
through a set of setter or getter methods that have the logging call added by default. 

The problem is that you can never be sure what will require an additional extension
in the future.  this simple fact often leads to over-encapsulation and a 
never-ending litany of setter and getter methods for every possible field 
that could otherwise be public.  

Thankfully, Python has a completely different approach to the accessor and mutator
pattern through the mechanisim of properties. Properties allow you to freely expose
public members of classes and simply convert them to getter and setter methods
whenever there is a such need.  and you can do that completely without breaking 
the backword compatibility of your class API.

```python

class UserAccount:
    def __init__(self, username, password):
        self._username = username
        self._password = password
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = value
```

The properties provide a built-in descriptor type that knows how to link an attritute 
to a set of methods. 
the property() function takes four optional arguments: 
fget, fset, fdel and doc.  the last one can be provided to define a docstring
function that is linked to the attribute as if it were a method.  


### 什么是 property？
Property 是一个特殊的**装饰器**，它允许你定义“getter”、“setter”和“deleter”方法，
用于将类的方法伪装成属性，**使得类的属性访问看起来像普通的属性操作： 你可以定义方法来控制属性的获取、设置和删除行为，但这些方法可以像普通属性**，但实际上背后有方法逻辑在运行。这种方式可以用来：
（装饰器： 初步理解为在方法体中添加装饰器方法的代码。）

 - 验证属性值。
 - 动态计算属性值。
 - 控制属性的读写权限。
 - 提供向后兼容性（例如将原本的属性改为方法，但保持接口不变）。

如何使用Property
property可以通过装饰器语法或者直接使用property()函数来使用
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # 私有变量

    @property
    def radius(self):
        """Getter: 获取半径"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter: 设置半径，并验证值是否有效"""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @radius.deleter
    def radius(self):
        """Deleter: 删除半径"""
        print("Deleting radius")
        del self._radius


# 使用
circle = Circle(5)
print(circle.radius)  # 调用 getter，输出: 5

circle.radius = 10  # 调用 setter
print(circle.radius)  # 输出: 10

del circle.radius  # 调用 deleter
```
使用property()方法调用
```python

class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    def del_radius(self):
        print("Deleting radius")
        del self._radius

    # 使用 property() 函数
    radius = property(get_radius, set_radius, del_radius, "The radius of the circle")


# 使用
circle = Circle(5)
print(circle.radius)  # 调用 getter，输出: 5

circle.radius = 10  # 调用 setter
print(circle.radius)  # 输出: 10

del circle.radius  # 调用 deleter

```

### 主要的用途： 提供对类属性的细粒度控制， 同时保证代码的简洁性和直观性
1， 属性验证
2， 动态计算属性值
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        """动态计算矩形面积"""
        return self.width * self.height


rect = Rectangle(4, 5)
print(rect.area)  # 输出: 20

```
3， 只读属性： 通过只定义 @property 而不定义 @<attr>.setter，可以创建只读属性。
```python
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


point = Point(1, 2)
print(point.x, point.y)  # 输出: 1 2
point.x = 3  # 抛出 AttributeError
```
4， 向后兼容性 ： 如果某个类的属性从简单的变量变成了复杂的逻辑，可以使用 property 来保持接口一致。

### IMPORTANCE
The best thing about the Python property mechanism is that it can be introduced to 
a class gradually.  逐步引入到类中 
You can start by exposing public attributes of the class instance and convert 
them to properties only if there is such a need.  
Other parts of your code won't notice any change in the class API because 
properties are accessed as if they were ordinary instance attributes. 

We've so far discussed the object-oriented data model of python in comparison to 
different programming language.But the data model is only a part of the OOP
language. 

The other importance factor of every object-oriented language is the 
approach to polymorphism (多态). Python provides a few implementations of 
polymorphism and that will be the topic of next section



