'''
    # 枚举扩展
'''

from enum import Enum
from enum import IntEnum, unique


@unique
class VIP(IntEnum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


print(type(VIP.GREEN.value))


