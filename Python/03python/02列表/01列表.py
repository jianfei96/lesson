list = [1,1.1,True,'string',[2,'string']]
print(list)
print(list[0])
print(list[-1])
print(list[4][0])

# 列表变量.count(数据) 数据在列表出现的数据
count = list.count('string')
print(count)

len = len(list)
print(len) #5个

# in 列表
# not in 判断存不存在

print(2 in list)
print(1 in list)