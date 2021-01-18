list1 = [1,1.1,True,'string',[2,'string']]
print(list1)
#del list1
#del list1[0:2]
#del list1[-1]
#list1.pop()  # [1, 1.1, True, 'string']

#移除数据本身 remove
list1.remove(1.1)

print(list1)

#清空数据
list1.clear()
print(list1)