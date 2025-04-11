from typing import Any
from warnings import warn

def ci_lookup() -> Any:
    pass

def __getattr__(name):
    if name == 'get_ci':
        warn(f'{name} is deprecated', DeprecationWarning)
        return ci_lookup()
    raise AttributeError(f'module {__name__} has no attribute {name}')

