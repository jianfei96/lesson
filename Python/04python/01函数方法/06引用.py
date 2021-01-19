#在python中，值是靠引用传递的 可以用id()判断

a = 1
b = a

print(id(a))
print(id(b))

#开辟新的地址存放a
a = 2

print(id(a))
print(id(b))
print(type(id(a)))

list1 = [10,20,30]
list2 = list1
# list2 = list1[:]

print(id(list1))
print(id(list2))

list1.append(40)
print(id(list1))
print(id(list2))
print(list1)
print(list2)

tuple1 = (10,20,30)
tuple2 = tuple1

print(id(tuple1))
print(id(tuple2))
tuple1 = (20,30,40)
print(id(tuple1))
print(id(tuple2))
print(tuple1)
print(tuple2)