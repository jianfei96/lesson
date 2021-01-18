set1 = {'string', True, 0, False, 1}  # 0和False，1和True不能共存

set1.add(100)
set1.add(200)
set1.add('10')
print(set1)

set1.update([10,20,30,'string'])
print(set1)
