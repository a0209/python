"""
    函数式编程
"""

# 匿名函数
f = lambda x, y: x + y
print(f(1, 2))

print('-----------------------')

# 三元表达式
x = 2
y = 3
r = x if x > y else y
print(r)

print('--------------------------')

# map函数
list_x = [1, 2, 3, 4, 5, 6, 7, 8]


def square(x):
    return x * x


r = map(square, list_x)
print(r)
print(list(r))

print('-----------------------')

# map和lambda
list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 2, 3, 4, 5, 6, 7, 8]

r = map(lambda x: x*x, list_x)
print(list(r))
r = map(lambda x, y: x*x+y, list_x, list_y)
print(list(r))

