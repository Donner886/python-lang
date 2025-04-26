### Functional programming
One of the great things about programming in Python is that you are never constrained to a single way of thinking about 
your programs. There are always various ways to solve a given problem, and sometimes the best one requires an approach
that is slightly different from the one that would be the most obvious. 
Sometimes, this approach requires the use of declarative programming. Fortunately, 
python, with its rich syntax and large standard library, offers features of functional programming, and functional
programming is one of the main paradigms of declarative programming. 

Functional programming is a paradigm where the program flow is archived mainly through the evaluation of functions
rather than through a series of  steps that change the state of the program.  Purely functional programs avoid the 
changing of state and the use of mutable data structures. 

One of the best ways to better understand the general concept of functional programming is by familiarizing yourself
with the basic terms of functional programming:
1. Side effects:
A function is said to have a side effect if it modifies the state outside of its local environment.  In other words, 
a side effect is any observable change outside of the function scope that happens as a result of a funciton call. 
An example of such side effect could be the modification of a global variable, the modification of an attribute of
an object that is available outside of the function scope, or saving data to some external service. 
Side effects are the core of concept of OOP, where class instances are objects that are used to  encapsulate the state
of an application, and methods are functions bound to those objects that are supposed to manipulate the state of the
object. Procedural programming also heavily relies on side effects. 
2. Referential transparency:  When a function or expression is referentially transparent, it can be replaced with the
value that is corresponds to its output with changing the behavior of the program.  
3. Pure functions： A pure function is a function that does not have any side effects and always returns the same value
for same set of input arguments. In other words, it is a function that is referentially transparent. 
Every mathematical function is, by definition, a pure function, 
4. First-class functions: Language is said to contain first-class functions if functions in this language can be treated
as any other value or entity.  First-class functions can be passed as arguments to other functions, returned as functnion
return values, and assigned to variables.  Functions in Python are first-class functions. 

Python offers a large variety of features that, for years, were only accessible in purely functional languages, Like:
1. Lambda functions and first-class functions
2. map(), filter(), and reduce() functions
3. Partial objects and functions
4. Generators and generator expression
Those features make it possible to write substantial amount of Python code in a functional way, even through Python 
is not purely functional. 

#### Lambda functions
Lambda functions are a very popular programming concept that is especially profound in functional programming. Lambda
function are anonymous functions that donot have to be bound to any identifier(variable).

Lambda functions in Python can be defined only using expressions.  The syntax for lambda functions is as follows:
lambda <arguments>:<expression>

Lambda functions are anonymous, but it does not mean they cannot be referred to using an identifier. Functions are the 
first-class objects, so whenever you use a function name, you're actually using a variable that is a reference to the 
function object. As with any other function, lambda functions are first-class citizens, so they can also be assigned to
a new variable. Once assigned to a variable, they are seemingly indistinguishable from other functions except for some 
metadata attribute. 

**The main use of lambda expression is to define contextual one-off funcntions that won't have to be resued elsewhere.**

Python provides a sorted() function that is able to sort any list as long as elements can be compared with at least 
"less than" comparison. We could define custom operator overloading on the person class, but we would have to know what 
field our records will be sorted on.  

Thankfully,  the sorted() function accepts the key keyword argument, which allows you to specify a function that will 
transform every element of the input into a value that can be naturally sorted by function. Lambda expression allow you 
to define such sorting keys on demand.  

sorted(people, key=lambda person: person.age)

#### the map(), filter(), and reduce() functions
the map(), filter(), reduce() function are three built-in functions that are most often used in conjunction with lambda
functions. They are commonly used in functional-style python programming because they allow us to declare 
transformation of any complexity, while simultaneously avoiding side effects.  

map(func, iterable...): applies the func function argument to every item of iterable.  you can pass more iterables to
the map() function. if you do so, map() will consume elements from each iterable simultaneously. the func function will 
receive as many arguments as there are iterables on every map step. if iterables are of different sizes, map() will stop
when the shortest one is exhausted.  It is worth remembering that map() does not evaluate the whole result at once, but
returns an iterator so that every result item can be evaluated only when it is necessary. 

filter(func, iterable):  works similarly to map() be evaluating input elements one by one. 
Unlike map(),  the filter() function does not transform input elements into new values, but allows us to filter out 
those input values that do not meet the predicate defined by the func argument.  

The reduce(func, iterable) function works in completely the opposite way to map().  As the name suggests, this function
can be used to reduce an iterable to a single value. Instead of taking items of iterable and mapping them to the func 
return values in one-by-one fashion, it cumulatively performs the operation specified by func over all iterable items. 

One interesting aspect of map() and filter() is that they can work on infinite sequences. The count() function from 
itertools is an example of a function that returns infinite iterables. it simply counts from 0 to infinity.  

**Unlike the map() and filter() functions, the reduce() function needs to evaluate all input items 
in order to return its value, as it does not yield intermediary results. This means that it cannot be used on 
infinite sequences.**



#### Partial objects and partial functions
Partial objects are loosely related to the concept of partial functions in mathematics.  
A partial function is a generalization of a mathematical function in a way that isn't 
forced to map every possible input value range (domain) to its results.  In Python, 
partical objects can be used to slice the possible input range of a given function by 
setting some of its arguments to a fixed value.  

Python provides a built-in function called pow(x, y) that can calculate any power of any number. 
So, our lambda x: x ** 2 expression is a partial function of the pow(x, y) function, 
because we have limited the domain values for y to a single value, 2.

在Python中，partial函数是functools模块中的一个工具，用于创建“部分应用函数”。 他的作用的固定某些函数参数的值， 从而生成一个
新的，更简单的函数。 这在某些场景下可以简化代码的逻辑提供代码质量。  

Partial的作用
当我们定义一个函数时，通常需要传入多个参数。如果某些参数的值是固定的， 或者我们希望提前绑定某些参数，那么可以使用partial来创建
一个新的函数， 这个新的函数只需接受剩余的参数既可。 
```python
from functools import partial

new_func = partial(func, *fixed_args, **fixed_kwargs)

# func: 原始函数
# *fixed_args： 要固定的位置参数
# **fixed_kwargs： 要固定的关键字参数



def add(a, b):
    return a + b

partial(add, b=1)(5) 

```

适用场景：
1. 简化回调函数： 当需要将一个函数作为回调函数传递时，如果该函数需要额外的固定参数，可以使用partial来简化。  
2. GUI编程的事件处理： 在GUI编程中，事件处理函数通常需要额外的上下文信息， 可以使用partial来绑定这些信息
```python
from functools import partial

def button_click_handler(button_name, event):
    print(f"{button_name} was clicked!")

# 绑定按钮名称
button1_handler = partial(button_click_handler, "Button 1")
button2_handler = partial(button_click_handler, "Button 2")

# 模拟按钮点击事件
button1_handler(None)  # 输出: Button 1 was clicked!
button2_handler(None)  # 输出: Button 2 was clicked!
```
3. 延迟计算： 可以延迟计算， 直到所有的参数提供为止。
```python

from functools import partial

def multiply(a, b):
    return a * b

# 创建一个延迟计算的函数
delayed_multiply = partial(multiply, 5)

# 等待用户提供另一个参数
result = delayed_multiply(10)
print(result)  # 输出: 50
```
注意事项： 
1. 不要过度使用：
- 如果逻辑过于复杂，建议直接定义一个新的函数，而不是依赖 partial。
  过度使用 partial 可能会让代码变得难以理解。
2. 不可变性：
- partial 创建的新函数不会修改原始函数的行为，也不会影响其他地方对原始函数的调用。
3. 调试困难：
- 使用 partial 后，函数的签名会丢失，可能会导致调试时难以追踪问题。