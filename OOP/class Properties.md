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


