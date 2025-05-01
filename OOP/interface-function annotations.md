### Interfaces through type annotations
Type annotations in Python proved to be extremely useful in increasing the quality of software.  
More and more professional programmers use mypy or other static type analysis tools by default, leaving conventional type-less
programming for prototypes and quick throwaway scripts.  

Support for typing in the standard library and community projects grew greatly in recent years.  Thanks to this, the flexibility
of typing annotations increases with every Python release. It also allows you to use typing annotations in completely new contexts. 

The core of structural subtyping is the typing.Protocol type. By subclassing this type, you can create a definition of your interface. 
the following is an example of base Protocol interfaces we could use in our previous example:

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class IBox(Protocol):
    x1: float 
    x2: float
    y1: float
    y2: float


@runtime_checkable
class ICollider(Protocol):
    
    @property
    def bounding_box(self) -> IBox:
        pass
```

As you can see, despite the fact that Python lacks native support for interfaces, we have plenty of ways to standardize contracts 
of classes, methods, and functions.  This ability becomes really useful when implementing various design pattern to solve 
commonly occurring programming problems.  Design patterns are all about reusability and the use of interfaces can help in 
structuring them into design templates that can be reused over and over again.  

But the use of interfaces does not end with design patterns. The ability to create a well-defined and verifiable contract for a 
single unit off code is also a crucial element of specific programming paradigms and technologies.  