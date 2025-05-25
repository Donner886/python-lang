### Metaprogramming

In This section, I want to know:

1. what is the metaprogramming in python?
2. how to conduct metaprogramming in  python?
3. what is the most common used usage via  metaprogramming in python?
4. other contribution in aspect of OOP

Many programmers associate it almost exclusively with programs that can inspect and manipulate their own code at source level.

Programs manipulating their own source code are definitely one of the most striking and complex examples of applied metaprogramming,

but metaprograming takes many forms and doesn't always have to be complex nor hard.

Python is expecially rich in features and modules that make certain metaprogramming techniques simple and natural.

In this chapter, we will explain what metaprogramming really is and present a few practical approaches to metaprogramming in Python. We will start with simple metaprogramming techniques like function and class decorators but will also cover advanced techniques to override

the class instance creation process and the use of metaclasses.  We will finish with examples of most powerful but also dangerous approach to  metaprogramming, which is code generation patterns.

Maybe we could find a good academic definition of metaprogramming, but this is a book that is more about good software craftsmanship than about computer science theory. this is why we will use our own informal definition of metaprogramming:

_"Metaprogramming is a technique of writing computer programs that can treat themselves as data, so they can introspect, generate, and/or modify themselves while running."_

Using this definition, we can distinguish between two major branches of metaprogramming in Python.  
1.  Introspect-oriented metaprogramming: Focused on natural introspection capabilities of the language and dynamic definitions of function and types.
2. Code-oriented metaprogramming: Metaprogramming focused on treating code as mutable data structures.  

Introspection-oriented metaprogramming concentrates on the language's ability to introspect its basic elements, such as functions, classes, or types, and to 
create or modify them on the go. Python really provides a lot of tools in this area. this feature of the python language is often used by 
Integrated Development Environments to provide real-time code analysis and name suggestions.  The easiest possible metaprogramming tools in python that utilize
language introspection features are decorators that allow for adding extra functionality to existing functions, methods, or classes.  
next are special methods of classes that allow you to interfere with the class instance creation process. the most powerful are metaclasses, which allow programmer 
to even completely redesign python's implementation of object-oriented programming.  

Code-oriented metaprogramming allows programmers to work directly with code, either in its raw(plain text) format or in the more programmatically accessible abstract syntax tree(AST) form.  
