#字符串.replace(‘旧的字符','新的字符',替换的次数) 返回修改后结果，新字符串
string = 'stringn'
#string = string.replace('n','m')
#string = string.replace('n','string',1)#替换一次
#string = string.replace('n','string',2)
print(string)

#字符串.split(‘分割的字符',分割的次数) 返回列表
# list = string.split('r') #['st', 'ingn']
# list = string.split('n',1) #['stri', 'gn']
list = string.split('n') #['stri', 'g', '']
print(list)

#字符串.join(list) 返回字符串
list = ['aa','bb','cc']
# str = '.'.join(list)
str = '-'.join(list)
print(str)