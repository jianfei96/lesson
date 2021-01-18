string = 'stringstring' 
#字符串.find('str') str是否在字符串中
#存在返回下标，不在返回-1
#find从左边查找，rfind从右边查找

print(string.find('t'))
print(string.rfind('t'))
print(string.find('tr'))
print(string.rfind('tr'))

print(string.find('a'))

print(string.count('s'))
print(string.count('string'))

#字符串.index('子字符串') 返回字符串下标，找不到报错
print(string.index('s'))

#ValueError: substring not found
#print(string.index('a'))