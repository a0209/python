'''
    练习
'''

print("hello world")

# 变量
A = [1, 2, 3, 4, 5, 6]
B = [1, 2, 3]
print(A * 3 + B + A)

a = 1
b = a
a = 3
print(b)

a = [1, 2, 3, 4, 5]
b = a
a[0] = '1'
print(a)
print(b)

a = [1, 2, 3]
print(id(a))
a[0] = '1'
print(id(a))

a = (1, 2, 3)
# a[0] = '1' 会报错

B = [1, 2, 3]
B.append(4)
print(B)

# 赋值运算符
a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c += a
print("2 - c 的值为：", c)

c *= a
print("3 - c 的值为：", c)

c /= a
print("4 - c 的值为：", c)

c = 2
c %= a
print("5 - c 的值为：", c)

c **= a
print("6 - c 的值为：", c)

c //= a
print("7 - c 的值为：", c)

# 比较运算符
a = 10
b = 20
print(a > b)

b = 1
b += b >= 1
print(b)

print('acd' > 'abc')

# 成员运算符
b = 'a'
print(b in {'c': 1})
b = 1
print(b in {'c': 1})
b = 'c'
print(b in {'c': 1})

# 身份运算符
a = 1
b = 1
print(a is b)

a = 1
b = 1.0
print(a is b)
print(id(a))
print(id(b))

a = {1, 2, 3}
b = {2, 1, 3}
print(a == b)
print(a is b)

c = (1, 2, 3)
d = (2, 1, 3)
print(c == d)
print(c is d)

# 条件控制
mood = False

if mood:
    print('go to left')
else:
    print('go to right')

ACCOUNT = 'qiyue'
PASSWORD = '123456'

print('please input account')
user_account = input()

print('please input password')
user_password = input()

if ACCOUNT == user_account and PASSWORD == user_password:
    print('success')
else:
    print('fail')

a = input()
print('a is ' + a)
print(type(a))
a = int(a)
if a == 1:
    print('apple')
elif a == 2:
    print('orange')
elif a == 3:
    print('banana')
else:
    print('shopping')

