'''
    枚举
'''

from enum import Enum


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


print(VIP.YELLOW)
print(VIP.YELLOW.value)
print(VIP.YELLOW.name)
print(VIP['YELLOW'])

print('------------')

# 遍历
for v in VIP:
    print(v)

print('---------------')

# 比较运算
result = VIP.GREEN is VIP.RED
print(result)

print('--------------------')


class VIP1(Enum):
    YELLOW = 1
    GREEN = 1
    BLACK = 3
    RED = 4


print(VIP1.GREEN)

print('----------------')

for x in VIP1.__members__.items():
    print(x)

# 枚举转换
a = 1
print(VIP1(a))

