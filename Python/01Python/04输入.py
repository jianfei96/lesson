# input('提示信息') 返回输入数据
password = input('password:')
print(password)
print(type(password))
# 转换数据类型
password = int(password)
print(password)
print(type(password))

password = str(password)
print(password)
print(type(password))

password = float(password)
print(password)
print(type(password))

# 不能转换成set list dict tuple
# 应该直接添加
# 元组tuple不可添加
""" password = set(password)
print(password)
print(type(password))
 """
