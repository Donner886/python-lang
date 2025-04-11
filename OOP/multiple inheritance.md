### Multiple inheritance and Method Resolution Order

Python MRO is based on C3 linearization, 在多重继承中，如果多个父类有相同的方法，Python 需要决定调用哪一个。Python 需要一种规则来决定 D 的方法调用顺序（MRO），而 C3 线性化 就是用来计算这个顺序的算法。
```python
class A:
    def foo(self):
        print("A.foo")

class B(A):
    def foo(self):
        print("B.foo")

class C(A):
    def foo(self):
        print("C.foo")

class D(B, C):
    pass

d = D()
d.foo()  # 应该调用 B.foo 还是 C.foo？
```


#### C3 线性化的规则。C3 算法的核心是 合并父类的线性化顺序，同时满足以下约束：
- 子类优先于父类（D 的 MRO 里，D 本身排在第一位）。
- 父类顺序不变（如果 class D(B, C)，则 B 的 MRO 应该在 C 之前）。
- **单调性**（如果 B是A的子类，B必须永远在A前	B→A 不能变成A→B）。
   - 确保了多继承的方法解析顺序（MRO）是 合理且一致 的，避免出现逻辑矛盾。

#### C3 线性化的计算步骤
假设我们有class D(B, C)，计算 D 的 MRO（D.__mro__）：
列出所有类的线性化（包括自己）：
1. L(D) = [D] + merge(L(B), L(C), [B, C])
   2. [B, C] 是 D 的直接父类声明顺序（class D(B, C)）
   3. "在计算 D 的 MRO 时，要合并 B 的 MRO、C 的 MRO，并确保 B 在 C 之前。"
2. L(B) = [B] + merge(L(A), [A]) = [B, A]
3. L(C) = [C] + merge(L(A), [A]) = [C, A]
4. L(A) = [A]
* 合并（merge）规则：
1. 从第一个列表的头部（第一个元素）开始检查：
2. 如果这个元素 没有在其他列表的尾部（非第一个位置），就把它加入 MRO，并移除所有列表中的该元素。
否则，跳过它，检查下一个列表的第一个元素。
计算 L(D)：
merge([B, A], [C, A], [B, C])
3. 检查 B（第一个列表的头）：
B 不在其他列表的尾部（[C, A] 的尾部是 A，[B, C] 的尾部是 C），所以选择 B。、
移除 B，得到 merge([A], [C, A], [C])
4. 检查 A： A 在 [C, A] 的尾部，不能选，跳过。
5. 检查 C（第二个列表的头）： C 不在 [A] 或 [C] 的尾部，选择 C。
移除 C，得到 merge([A], [A], [])
6. 最后选择 A。  最终 L(D) = [D, B, C, A]
* 验证：
```python
print(D.__mro__)  # 输出: (D, B, C, A, object)
```
* 如果 C3 算法失败？
1. 如果 C3 无法找到合法的 MRO（比如出现冲突），Python 会抛出 TypeError：
```python
class A: pass
class B(A): pass
class C(A, B): pass  # TypeError: Cannot create a consistent method resolution
```
A 必须在 B 之前（C(A, B)），但 B 是 A 的子类，违反 单调性。


