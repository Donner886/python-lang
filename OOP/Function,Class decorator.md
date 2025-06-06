### Python decorator 终极详解
Decorator(装饰器)是python中一种强大的语法特性， 它允许在不修改原始代码的情况下动态地扩展或修改函数的行为。  装饰器（decorator）实在函数/类定义时就完成了
扩展或修改。 当python解释器遇到装饰器语法时会立即执行装饰器逻辑。 
#### Function Decorator 函数装饰器
Function Decorator 是一个可调用对象  *可调用对象（callable）指的是可以像函数那样被调用的对象。这意味着你可以在其后加上一对圆括号()并传入参数来执行某些操作。所有可调用对象都有一个共同点：它们实现了特殊的__call__()方法。当你尝试调用一个对象时，Python解释器会自动调用这个对象的__call__()方法。*
它接受一个函数作为输入并返回一个新的函数。 装饰器是一种操作函数的函数， 它遵循“函数也是一等对象 （first-class object）”的原则。 
核心概念：
1. 函数是对象， 可以赋值给变量
2. 函数可以嵌套定义 （闭包）
3. 函数可以作为参数传递

```python
def funcDecorator(func):
    print(f'Decorating function {func.__name__}')
    def wrapper(*arg, **kwargs):
        ## 调用原函数前的逻辑
        print(f"Before calling {func.__name__}")
        ## 调用原函数
        result = func(*arg, **kwargs)
        ## 调用源函数后逻辑
        print(f"After calling {func.__name__}")
        return result
    return wrapper

@funcDecorator
def myFunc(a, b):
    print('My Function 执行中........')
    return a +  b
##output: Decorating function myFunc

myFunc(1,1)
##output: 
# Before calling myFunc
# My Function 执行中........
# After calling myFunc
```
工作原理： 当使用@funcDecorator装饰myfunc时，python实际上执行的是myfunc = funcDecorator(myFunc)， 当调用myFunc时， 实际上调用的是wrapper()函数

```python
## 带参数的函数装饰器
def repeat(num_times):
    print(f'接受装饰器参数：{num_times}')
    ## 这个外层函数， 接收装饰器参数 /////
    def decorator_repeat(func):
        print(f'确认函数名称：{func.__name__}')
        ## ////这才是真正的装饰器/////
        def wrapper(*args, **kwargs):
            print(f'num of times: {num_times},  Before {func.__name__} execute')
            for _ in range(num_times):
               result = func(*args, *kwargs)
            print(f'num of times: {num_times},  After {func.__name__} execute')
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=4)
def greet(name):
    print(f'{greet.__name__} is running now.')
    print(f"Hello {name}")

## output: 
# 接受装饰器参数：4
# 确认函数名称：greet


greet('ddma')

## output:  
# num of times: 4,  Before greet execute
# wrapper is running now.
# Hello ddma
# wrapper is running now.
# Hello ddma
# wrapper is running now.
# Hello ddma
# wrapper is running now.
# Hello ddma
# num of times: 4,  After greet execute

```
装饰器语法@decorator实际是一种语法糖， 等价与decoratedFunc = decorator(decoratedFunc)。
当python解释器遇到装饰器时，它会：
1. 立即执行装饰器函数（在模块导入时） 
2. 将被装饰的函数作为参数传递给装饰器
3. 用装饰器返回的函数替换原函数
Note: 装饰器会掩盖原函数的元数据， (如: \_\_name__  , __doc__等)， 需要使用functools.wraps来保留。 
在Python中，带参数的装饰器的等价转换过程比普通的装饰器多了一层嵌套。   
```python
@decorator
def func():
    pass
```
这实际上是一个三层嵌套的过程， 等价于： 
func = decorator(params)(func) , 第一步： 先调用decorator(params)，返回真正的装饰器函数； 第二步: 用返回的装饰器处理目标函数； 、
为什么需要三层结构呢： 1， 最外层接收装饰器参数， 2， 中阶层处理被装饰函数， 3， 最内层处理实际调用逻辑



