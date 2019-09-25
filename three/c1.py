"""
    闭包 = 函数 + 环境变量
"""


def curve_pre():
    a = 25

    def curve(x):
        return a * x * x

    return curve


a = 10
f = curve_pre()
print(f.__closure__)
print(f.__closure__[0].cell_contents)
print(f(2))

print('------------------------------')


def f1():
    a = 10

    def f2():
        a = 20
        print(a)
    print(a)        # 10
    f2()            # 20
    print(a)        # 10


f1()

print('--------------------------------')


origin = 0


def go(step):
    global origin   # 把局部变量=>全局变量
    new_pos = origin + step
    origin = new_pos
    return new_pos


print(go(2))
print(go(3))


