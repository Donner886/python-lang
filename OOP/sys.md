### SYS
Some modules in the standard library, such datetime and pickle, have identical implementations in C and Python; the C 
implementation, when available, is expected to improve performance(such extension modules are commonly referred to as accelerator modules)

Other modules mainly implemented in Python may import a C helper extension providing implementation details. 
(for instance, the csv module uses the internal _csv module defined in Modules/_csv.c).

Classify extension modules.
1. A built-in extension module is a module built and shipped with the python interpreter. A built-in module is statically
linked into the interpreter, thereby lacking a __file__ attribute.
```python
import sys
sys.builtin_module_names

## output: 
('_abc',
 '_ast',
 '_bisect',
 '_blake2',
 '_codecs',
 '_codecs_cn',
 '_codecs_hk',
 '_codecs_iso2022',
 '_codecs_jp',
 '_codecs_kr',
 '_codecs_tw',
 '_collections',
 '_contextvars',
 '_csv',
 '_datetime',
 '_functools',
 '_heapq',
 '_imp',
 '_io',
 '_json',
 '_locale',
 '_lsprof',
 '_md5',
 '_multibytecodec',
 '_opcode',
 '_operator',
 '_pickle',
 '_random',
 '_sha1',
 '_sha256',
 '_sha3',
 '_sha512',
 '_signal',
 '_sre',
 '_stat',
 '_statistics',
 '_string',
 '_struct',
 '_symtable',
 '_thread',
 '_tokenize',
 '_tracemalloc',
 '_typing',
 '_warnings',
 '_weakref',
 '_winapi',
 '_xxsubinterpreters',
 'array',
 'atexit',
 'audioop',
 'binascii',
 'builtins',
 'cmath',
 'errno',
 'faulthandler',
 'gc',
 'itertools',
 'marshal',
 'math',
 'mmap',
 'msvcrt',
 'nt',
 'sys',
 'time',
 'winreg',
 'xxsubtype',
 'zlib')
```
2. A shared (or dynamic) extension module is built as a shared library (.so or .dll file) and is dynamically linked to the interpreter.  
in particular, the module's __file__ attribute contains the path to the .so or .dll file.

[https://devguide.python.org/developer-workflow/extension-modules/](https://devguide.python.org/developer-workflow/extension-modules/)


