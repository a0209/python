"""
    有一个或多个参数的装饰器使用
"""

import time


def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper


@decorator
def f1(func_name):
    print('This is ' + func_name)


@decorator
def f2(func_name1, func_name2):
    print('This is ' + func_name1)
    print('This is ' + func_name2)


@decorator
def f3(func_name1, func_name2, **kw):
    print('This is ' + func_name1)
    print('This is ' + func_name2)
    print(kw)


f1('test')
f2('test2.1', 'test2.2')
f3('test3.1', 'test3.2', a=1, b=2, c='1,2,3')
