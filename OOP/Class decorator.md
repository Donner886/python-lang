## Class Decorator (类装饰器)
Class decorator是一个可调用对象，  他接受一个累作为输入并返回一个新的修改后类。类装饰器可以修改类的属性，方法，甚至完全替换类。  
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
2. 然后将这个类对象传递给装饰器函数
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
