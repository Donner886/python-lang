### Intercepting the class instance creation process （拦截类实例的创建过程） 
There are two special methods concerned with the class instance creation and initialization process. These are \__init__()
and \__new__()
the \__init__() method is the closest to the concept of the constructor found in many OOP programming language. It receives 
a fresh class instance together with initialization arguments and is responsible for initializing the class instance state.  
The \__new__() method is a static method that is actually responsible for creating class instances. This \__new__(cls, [,.....])
method is called prior to the \__init__() initialization method. Typically, the implementation of the overriden \__new__() method
invokes its superclass version using super.\__new__() with suitable arguments and modifies the instance before returing it.  

