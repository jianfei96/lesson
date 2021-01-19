def user(name,age,gender):
    print(f'name:{name},age:{age},gender:{gender}')

user(20,'rose','m')
#数据传递顺序不同
user(age=20,name='rose',gender='m')

# *接收元组类型
def user_tuple(*args):#前面加*为元组
    print(args)

user_tuple('tom',20)

# ** 接受字典数据类型的值

def user_dict(**dicts):
    print(dicts)

user_dict(name='tom',age=20)

#在python中，值是靠引用传递的 可以用id()判断