"""
    reduce
"""

from functools import reduce
import re

# 连续计算, 连续调用lambda
list_x = ['1', '2', '3', '4']
list_y = [1, 2, 3, 4]
r = reduce(lambda x, y: x+y, list_x)
print(r)
r = reduce(lambda x, y: x+y, list_y)
print(r)
r = reduce(lambda x, y: x+y, list_x, 'aaa')
print(r)

print('-------------------')

# filter
list_x = [1, 0, 1, 0, 0, 0, 1]
r = filter(lambda x: x, list_x)
print(r)
print(list(r))

list_z = ['a', 'B', 'C', 'd', 'E']
r = filter(lambda x: re.findall('[a-z]', x), list_z)
print(r)
print(list(r))


