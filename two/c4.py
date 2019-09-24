'''
    JSON
'''

# 反序列化
import json

json_str = '{"name": "siyue", "age": 18}'

s = json.loads(json_str)
print(type(s))
print(s)

print('---------------------')

# 序列化
x = [
        {'name': 'siyue', 'age': 18, 'flag': False},
        {'name': 'guoguo', 'age': 28}
    ]

j_str = json.dumps(x)
print(type(x))
print(type(j_str))
print(j_str)