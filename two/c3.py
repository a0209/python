'''
    正则表达式
'''

import re

a = 'C|C++|Java|C#|Python|Javascript|Python'

r = re.findall('Python', a)
print(r)

if len(r) > 0:
    print('字符串中包含Python')
else:
    print('NO')

print('-------------------')

# 元字符
a = 'C0C++9Java7C#6Python4Javascript'
x = re.findall('\d', a)
print(x)
x = re.findall('\D', a)
print(x)

print('---------------')

# 字符集
s = 'abc, acc, adc, aec, afc, ahc'

r = re.findall('a[cf]c', s)
r = re.findall('a[^cf]c', s)
r = re.findall('a[c-h]c', s)
print(r)

print('-------------')

# 数量词
a = 'python 1111java678php'

r = re.findall('[a-z]{3,6}', a)
print(r)

print('---------------')

# 贪婪 与 非贪婪  默认贪婪
a = 'python 1111java678php'

r = re.findall('[a-z]{3,6}?', a)
print(r)

print('-------------')

# 数量词2
a = 'pytho0python1pythonn2'

r = re.findall('python*', a)
r = re.findall('python+', a)
r = re.findall('python?', a)
print(r)

print('--------------')

# 边界匹配
qq = '100000001'    # 9位

r = re.findall('^\d{4,8}$', qq)
print(r)

print('--------------')

# 组
a = 'PythonPythonPythonPythonPython'

r = re.findall('(Python){3}', a)
print(r)

print('---------------')

# 模式参数
language = 'PythonC#\nJavaPHP'

r = re.findall('c#.{1}', language, re.I | re.S)
print(r)

print('---------------')

# re.sub 正则替换
l = 'PythonC#JavaC#PHPC#'


def convert(value):
    matched = value.group()
    return '!!' + matched + '!!'


r = re.sub('C#', 'GO', l)
r = re.sub('C#', 'GO', l, 1)
r = re.sub('C#', convert, l)
print(r)

s = 'A8C3721D86'

def convert1(value):
    matched = value.group()
    if int(matched) >= 6:
        return '9'
    else:
        return '0'

r = re.sub('\d', convert1, s)
print(r)

print('----------------')

s = 'A8C3721D86'

r = re.match('\d', s)
print(r)
r1 = re.search('\d', s)
print(r1)
print(r1.span())
print(r1.group())

print('-----------------')

s = 'life is short,i use python, i love python'

r = re.search('life(.*)python(.*)python', s)
print(r.group(0, 1, 2))
print(r.groups())
r = re.findall('life(.*)python(.*)python', s)
print(r)

