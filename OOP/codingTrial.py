# class ABCMeta(type):
#     def __instancecheck__(cls, instance):
#         return any(cls.__subclasscheck__(c) for c in {type(instance), instance.__class__ })
#
#     def __subclasscheck__(cls, subclass):
#         candidates = cls.__dict__.get("__subclass__", set()) | {cls}
#         return any(c in candidates for c in subclass.mro())
# class Sequence(metaclass=ABCMeta):
#     __subclass__  = {list, tuple}
#
# assert issubclass(list, Sequence)
#


from abc import ABCMeta, abstractmethod
class MyABC(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass
class MyABC_ins1(MyABC):

    def foo(self):
        print('overriding foo method derided from MYABC')

## MyABC_ins1()
## TypeError: Can't instantiate abstract class MyABC_ins1 without an implementation for abstract method 'foo'


class abstractproperty(property):
    __isabstractmethod__ = True

from collections import