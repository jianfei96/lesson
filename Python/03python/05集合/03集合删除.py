set1 = {'string', True, 0, False, 1, 2}  # 0和False，1和True不能共存
print(set1)

set1.remove(1)
#set1.remove(20) #删除不存在的值会报错
print(set1)

set1.discard(20) #discard不报错
#set1.discard(2)
print(set1)

print(set1.pop())
print(set1)
