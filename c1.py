
# while循环
counter = 1
while counter <= 10:
    counter += 1
    print(counter)
else:
    print('EOF')

# while counter: print('YES')

# for循环
a = [1, 2, 3]
for x in a:
    # if x == 2
        # break
        # continue
    print(x)
else:
    print('EOF')

a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
for x in a:
    for y in x:
        if y == 'orange':
            break
        print(y)
else:
    print('fruit is gone')

# range()
for i in range(5):
    print(i)    # 0 1 2 3 4

for i in range(5, 9):
    print(i)    # 5 6 7 8

for i in range(0, 10, 3):
    print(i)    # 0 3 6 9

for i in range(10, 0, -3):
    print(i)    # 10 7 4 1

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = len(a)
print(b)
for c in range(1, b, 2):
    print(c)

print(a[0:len(a):2])

# import 和 from...import
'''
import one.c1
from one.c1 import *
from one.c1 import b
print(b)
'''

# import one
# print(one.sys.path)

# import sys
# sys.setrecursionlimit(100000)     设置循环递归的次数

# 函数


def add(x, y):
    result = x + y
    return result


def print_code(code):
    print(code)


a = add(1, 2)
b = print_code('Python')

print(a, b)

# 让函数返回多个结果


def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    return damage1, damage2


skill1_damage, skill2_damage = damage(3, 6)     # 序列解包
print(skill1_damage, skill2_damage)

# 序列解包
a = 1
b = 2
c = 3

a, b, c = 1, 2, 3

d = 1, 2, 3
print(type(d))

a, b, c = d     # 序列解包

a = b = c = 1   #链式赋值


def adds(x, y):
    result = x + y
    return result


c = adds(y = 3, x = 2)	# 关键字参数 代码的可读性

# 默认参数


def print_student_files(name, gender='男', age=18, college='人民路小学'):
    print('我叫' + name)
    print('我是' + gender + '生')
    print('我今年' + str(age) + '岁')
    print('我在' + college + '上学')


print_student_files('鸡小萌')

print('----------------------')


# print_student_files('果果', gender='女', 17, college='光明小学')  位置参数不能跟在关键字参数后面
def adds(x, y):
    result = x + y
    return
    print('1111');


c = adds(3, 2)
print(c)

print('--------------------')

from one.c1 import Student

student = Student()
student.print_file()
