list1 = [1,1.1,True,'string',[2,'string']]
print(list1)

list1[0] = 2
print(list1)

# 列表.sort() 默认升序
# list1.sort() #TypeError: '<' not supported between instances of 'str' and 'bool'
list2 = [1,3,2,'4','0'] #TypeError: '<' not supported between instances of 'str' and 'int'
list2 = [1,3,2,4,0]
list2.sort()
print(list2)