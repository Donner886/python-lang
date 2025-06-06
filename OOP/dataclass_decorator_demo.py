from typing import Any, Iterable

import setuptools.package_index

UNSET = object()

def repr_instance(instance: object, attrs: Iterable[str]) -> str:
    """
     override the object representation function with one can show specific attributes and related values
    :param instance:
    :param attrs:
    :return:
    """
    attr_values: dict[str, Any] = {
        attr: getattr(instance, attr, UNSET)
        for attr in attrs
    }
    sub_repr = ",".join(
        f"{attr}={repr(val) if val is not UNSET else 'UNSET'}"
        for attr, val in attr_values.items()
    )
    return f"<{instance.__class__.__qualname__}:{sub_repr}>"



def autorepr(cls):
    """
    Get annotated attributes automatically and set their in representation function.
    :param cls:
    :return:
    """
    attrs = set.union(
        *(
            set(c.__annotations__.keys())
            for c in cls.mro()
            if hasattr(c, "__annotations__")
        )
    )

    def __repr__(self):
        return repr_instance(self,sorted(attrs))
    cls.__repr__ = __repr__
    return cls

@autorepr
class MyClass:
    attr_1: Any
    attr_2: Any
    attr_3: Any

    def __init__(self, a, b):
        self.attr_1 = a
        self.attr_2 = b

def autorepr2(cls):
    attrs = cls.__annotations__.keys()
    class Klass(cls):
        def __repr__(self):
            return repr_instance(self, attrs)

    return Klass

