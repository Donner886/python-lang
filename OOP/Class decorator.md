## Class Decorator (类装饰器)
_Class decorator是一个可调用对象，他接受一个类作为输入并返回一个新的修改后类。类装饰器可以修改类的属性，方法，甚至完全替换类。_  

### 1. 函数作为类装饰器
```python

def class_decorator(cls):
    ## update or add class attribute
    cls.new_attribute = 'Add by decorator!!!'
    ## update a class method
    original_method =cls.method
    
    def wrapped_method(self, *args, **kwargs):
        print(f'Decoraor: before method')
        result = original_method(self, *args, **kwargs)
        print(f'Decoraor: After method')
        return result
    cls.method = wrapped_method
    
    ## add a new method
    def new_method(self):
        print(f'This is a new method')
    cls.new_method = new_method
    
    return cls 

```
工作原理： 类装饰器的工作流程
1. 当python解释器遇到类定义时， 会先创建类对象
2. 然后将这个类对象传递给类装饰器函数
3. 装饰器返回的类会替换原始类


PS. 在python中，当解释器遇到类定义时创建的“类对象”， 本质上是一个type实体， 同时也是该类的类实体，两个表述实际上是同一事物的不同视角。 

| 术语 | 本质| 相互关系 |
|----------|------|------------|
| 类对象|	Python 中所有类都是运行时创建的对象	|既是 type 的实例，又是其子类的父类|
| class entity	|用户视角的"类"（如 class MyClass）	|在 Python 实现中就是 type 或其子类的实例|
|type entity	|元类视角的"类型"（所有类对象的类型都是 type 或其子类）|	类是 type 的实例，type 是自己的元类|

类创建过程的本质： 当解释器执行类定义时， 如class MyClass， 会按照如下步骤创建对象： 
1. 收集类成员： 解释器会收集x和method到临时命名空间
```python
class Myclass:
    x = 10
    def method(self):
        pass
```
2. 调用元类构造， 底层等价于如下。 此时创建的Myclass即是用户可见的类， 也是type的实例。 
```python

Myclass = type(
    'Myclass',
    (object,),
    {'x':10, 'method': method}
)

print(type(Myclass))
# output 
##<class 'type'>
print(isinstance(Myclass, type))
## output
## True
```



### 2. 类作为类装饰器
```python
class ClassDecorator:
    def __init__(self, cls):
        self.cls = cls
    
    def __call__(self, *args, **kwargs):
        ### 在这里修改实例创建过程
        instance  = self.cls(*args, **kwargs)
        ## 添加实例属性
        instance.decorated = True 
        return instance

my_class = ClassDecorator(Myclass)
```

### Class Decorator的使用场景
1. 类注册
2. 添加类属性/方法
3. 修改类属性/方法
4. 实现接口/抽象类
5. ORM映射

### 不足：
1. 复杂性高：实现通常比函数装饰器更复杂
2. 可读性差：可能使代码更难理解，特别是当深度修改类时
3. 维护困难：装饰器顺序有时很重要且容易出错
4. 过度设计风险：可能诱使开发者创建过于复杂的类层次结构


 使用 Class Decorator 的知名包
Django REST framework (API 框架)
@decorators.api_view - API 视图装饰器
@decorators.permission_classes - 权限类装饰器

Pytest (测试框架)
@pytest.mark.usefixtures - 类级别夹具使用

SQLAlchemy (ORM)
@as_declarative - 声明式基类装饰器

一些实验性的类装饰器
attrs (类工具库)
@attr.s - 类似于 @dataclass 但功能更强大

Zope (组件架构)
各种类装饰器用于组件注册和适配

Pyramid (Web 框架)
一些类级别的配置装饰器

Pydantic (数据验证)
某些类装饰器用于模型配置


5.3 同时使用两种装饰器的包
许多现代 Python 包会根据不同需求同时使用两种装饰器：
FastAPI：同时使用函数装饰器 (@app.get) 和类装饰器 (依赖注入系统)
TensorFlow/Keras：使用函数装饰器定义模型，类装饰器定义层
Scikit-learn：使用类装饰器进行估计器注册


