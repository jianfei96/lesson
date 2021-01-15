'''
1 按需求定义变量
2 验证数据 type()
'''

number = 1
print(number)
print(type(number))

numberfloat = 1.1
print(numberfloat)
print(type(numberfloat))

string = 'string'
print(string)
print(type(string))

boolean = True
print(boolean)
print(type(boolean))

# 列表 可以存放不同数据类型，可修改
list1 = [1, 1.1, 'str']
print(list1)
print(type(list1))

# tuple 元组 存放不同类型数据，不可修改
tuple1 = (1, 1.1, 'str')
print(tuple1)
print(type(tuple1))

# list1[1] = '1.1'
# print(list1)
# tuple1[1] = '1.1' #tuple不可修改
# print(tuple1)

# set 集合 集合去掉重复数据 集合无序 不支持下标
set1 = {1, 1, 1.1, 'str'}
print(set1)
print(type(set1))

# dict 字典 键值对
dict1 = {'name': 'tom', 'age': 20}
print(dict1)
print(type(dict1))
print(dict1['name'])
