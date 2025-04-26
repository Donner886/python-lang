### Generators
Generators provide an elegant way to write simple and efficient code for functions
that return a sequence of elements.  **Based on the yield statement, they allow you to 
pause a function and return an intermedia result.** The function saves its execution 
context and can be resumed later, if necessary. 

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield b 
        a, b = b, a +b
```

Our fibonacci() function returns a generator object, a special iterator that knows how to save
the execution context. It can be called indefinitely, yielding the next element of the sequence 
each time.  the syntax is concise, and the infinite nature of the algorithm does not disturb the
readability of the code. It does not have to provide a way to make the function stoppable. In fact, 
it looks similar to how the sequence generating function would be designed in psuedo code. 

In many cases, the resources required to process one element are less than the resources required
to store whole sequences. Therefore, they can be kept low, making the program more efficient. 
For instance, the Fibonacci sequence is infinite, and yet the generator that generates it does not 
require an infinite amount of memory to provide the values one by one,theoretically, could work 
ad infinitum.  
A common use case is to stream data buffers with generators.  They can be paused, resumed, and stopped
whenever necessary at any stage of the data processing pipeline without any need to load whole datasets
into the program's memory. 

In functional programming, generators can be used to provide a useful function that otherwise would require
saving intermediary result as side effects as if it were a stateless function.  


### Generator expressions
Generator expressions are another syntax element that allows you to write code in more functional way. 
Its syntax is similar to comprehensions that are used with dictionary, set and list literals.
List字面量的解析式
A generator expression is denoted by parentheses, like in the following example:
(item for item in iterable_expression)
**Generator expressions can be used as input arguments in any function that accepts iterables.  
They also allow if clauses to filter specific elements the same way as list, dictionary, and set
comprehensions.  This means that you can ofter replace complex map() and filter() constructions with more 
readable and compact generator expressions. 

Syntactically, generator expressions are no different from any other comprehension expression. Their main
advantage is that they evaluate only one item at a time.  So if you process an arbitrarily long iterable 
expression, a generator expression may be a good fit as it doesn't need to fit the whole collection of 
intermediary results into program memeory.  


## Decorators
The decorator is generally a callable expression that accepts a single argument when called. and returns another
callable object. 
While decorators are often discussed in the scope of methods and functions. they are not limited to them.  
in fact, anything that is callable(any object that implements the __call__ method is considered callable)
can be used as a decorator, and often, objects returned by them are not simple functions but are instances of
more complex classes that are implementing their own __call__ method. 

The decorator syntax is simply syntactic sugar. Consider the following decorator usage:  

```python
@some_decorator
def decorated_functions():
    pass
```

This can always be replaced by an explicit decorator call and function reassignment:
```python
def decorated_function():
    pass
decorated_function = some_decorator(decorated_function)
```
However, the latter is less readable and also very hard to understand if multiple decorators are used on a single 
function.

** Decorator are elements of the programming language inspired by aspect-oriented programming and the decorator
design pattern. the main use case is to conveniently enhance an existing function implementation with extra behavior
coming from other aspects of your application.  

```python
@app.route('/secret_page')
@login_required
def secret_page():
    pass
```
According to the single-responsibility principle, functions should be rather small and single-purpose. In our Flast application, 
the secret_page() view function would be responsible for preparing the HTTP response that can be later rendered in a web 
browser.  It probably shouldn't deal with things like parsing HTTP requests, verifying user credentials, and so on.  
As the names suggests, the secret_page() function returns something that is secret, and should not be  visible to anyone. 
Verifying user credentials is not part the view function's responsibility but it is part of the general idea of
"a secret page". The @login_required decorator allows you to bring the aspect of user authentication close to the view
function. it makes the application more concise and the intent of the programmer more readable.  

```python
from functools import wraps
from flask import  g, request, redirect, url_for

def login_require(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next(request.url)))
        return f(*args, **kwargs)
    return decorated_function
```
The @wraps decorator allows you to copy decorated function metadata like name and type annotations.  it is a good practise
to use the @wraps decorator in your own decorators as it eases debugs and gives access to original function type annotations. 
The login requirement may be a common aspect of applications, but the impelmentation of that aspect can change over time.  
Decorators offer a convenient way of pack such aspects into portable behaviors that can be easier added on top of exsiting
functions. 



#### Enumerations
There are common programming features that are found in many programming language regardless of the dominant programming 
paradigm.  One such feature is enumerated types that have a finite number of named values. 
They are especially useful for encoding a closed set of values for variables or function arguments. 
One of the special handy types found in the python standard library is the Enum class from the enum module. 
this is a base class that allows you to define symbolic enumerations. 
In order to define your own enumeration in Python,   

In order to define your own enumeration in Python, you will need to subclass the Enum class and define all Enumeration 
members as class attributes. 
```python
from enum import Enum
class WeekDay(Enum):
    MONDAY = 0
    THESDAY = 1
    WEDNESDAY = 3

```
Enumerations in Python are really useful in every place where some variable can take only a 
