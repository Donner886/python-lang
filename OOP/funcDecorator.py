def funcDecorator(func):
    print(f'Decorating function {func.__name__}')
    def wrapper(*arg, **kwargs):
        ## 调用原函数前的逻辑
        print(f"Before calling {func.__name__}")
        ## 调用原函数
        result = func(*arg, **kwargs)
        ## 调用源函数后逻辑
        print(f"After calling {func.__name__}")
        return result

    return wrapper