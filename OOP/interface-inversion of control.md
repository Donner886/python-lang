#### Inversion of control and dependency injection
Inversion of Control (IoC) is simple property of some software designs.  According to Wiktionary, if a design exhibits  IoC,
it means that: the flow of control in a system is inverted in comparison to the traditional architecture.  
IoC isnot a new idea, and we can trace it back to at least David D.Clark's paper from 1985 titled The structuring of systems 
using of upcalls.  It means that traditional design probably refers to the design of software that was common or thought to be 
traditional in the 1980s.

Clarks describes the traditional architecture of a program as a layered structure of procedures where control always goes from 
top to bottom. Higher-level layers invoke procedures from lower layers.  Those invoked procedures gain control and can invoke
even deeper-layered procedures before returning control upward. In practise, control is traditionally passed from application 
to library functions. Library functions may pass it deeper to even lower-level libraries but, eventually, return it back to the 
application.  

**IoC happens when a library passes control up to the application so that the application can take part in the library behavior. **
To better understand this concept consider the following trivial example of sorting a list of integer numbers:
```python
sorted([1,3,4,2,5])
```
The built-in sorted() function takes an iterable of items and returns a list of sorted items.  Control goes from the caller(your application)
directly to the sorted() function. When the sorted() function is done with sorting, it simply returns the sorted result and gives 
control back to the caller. Nothing special. 
Now, let's say we want to sort our numbers in a quite unusual way.  That could be, for instance, sorting them by the absolute 
distance from number 3. Integers closet to 3 should be at the beginning of the result list and the farthest should be the end. 
we can do that by defining a simple key function that will specify the order key of our elements:
```python
def distance_from_3(item):
    return abs(item - 3)

sorted([1,3,4,2,5], key=distance_from_3)

```
What will happen now is the sorted() function will  invoke the key function on every element of the iterable argument. 
Instead of comparing item values, it will now compare the  return values of the key function.  Here is where IoC happens. 
the sorted() function "upcalls" back to the distance_from_3() function provided by the application as an argument.
*Now it is a library that calls the functions from the application, and thus the flow of control is reversed.*

Note that IoC is just a property of a design and not a design pattern by itself. An example with the sorted() function is 
the simplest example of callback-based IoC but it can take many different forms. 
1. Polymorphism:  When a custom class inherits from a base class and bases methods are supposed to call custom methods. 
2. Argument passing: When the receiving functions is supposed to call methods of the supplied object. 
3. Decorators: when a decorator function calls a decorated function
4. Closures: When a nested function calls a function outside of its scope. 

As you see, IoC is rather common aspect of object-oriented or functional programming paradigms. And it also happens quite
often without you even realizing it.  While it isnot a design pattern by itself, it is a key ingredient of many actual design 
patterns, paradigms, and methodologies. The most notable one is dependency injection, whill we will discuss later in this chapter.  

### Inversion of control in applications
To better illustrate the differences between various flows of control, we will build a small but practical application. 
It will initially start with a traditional flow of control and later on, we will see if it can benefit from IoC in selected places. 
Our use case will be pretty simple and common. We will build a service that can track web page views using so-called tracking pixels
and serve page view statistics over an HTTP endpoint. 
```python
@app.route('/route')
def track():
    pass
```
This is the first occurrence of IoC in our application: we register our own handler implementation within Flask frameworks. 
It is a framework that will call back our handlers on incoming requests that match associated routes.


### Using dependency injection frameworks
When IoC is used at a great scale, it can easily become overwhelming. The example from the previous section was quite simple 
so it didn't require a lot of setup.  
Unfortunately, we have sacrificed a bit of readability and expressiveness for better modularity and responsibility isolation. 
For larger applications, this can be a serious problem. 
Dedicated dependency injection libraries comes to the rescue by combining a simple way to mark function or object dependencies
with a runtime dependency resolution.  All of that usually can be achieved with minimal impact on the overall code structure.  

There are plenty of dependency injection libraries for Python, so definitely there is no need to build your own from scratch. 
they are often similar in implementation and functionality， so we will simply pick one and see how it could be applied 
in our views tracking application. 

Our library of choice will be the injector library, which is freely available on PyPI. We will pick it up for several reasons:
1. Reasonably active and mature. Developed over more than 10 years with releases every few months
2. Framework support: It has community support for various Framework including flask through flask-injector package.
3. Typing annotation support: It allows writing unobtrusive dependency annotations and leveraging static typing analysis.
4. Simple: injector has a Pythonic API. It makes code easy to read and to reason about.