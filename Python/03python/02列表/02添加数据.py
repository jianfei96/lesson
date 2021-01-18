list = [1,1.1,True,'string',[2,'string']]
#列表数据允许修改
list.append('list')
list.append(['list','string']) #添加一个列表元素
list.extend(['list','string']) #添加整个列表，读取列表数据逐个添加
print(list)

list.insert(0,'insert') #指定位置插入数据
print(list)
