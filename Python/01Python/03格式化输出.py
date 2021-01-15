age = 18
name = 'tom'
weight = 60.0
id = 1
# %变量会替换字符串中%d位置
print('age:%d' % age)
print('name:%s' % name)
print('weight:%f' % weight)
print('id:%d' % id)
# %.2f 显示小数点后两位
print('weight:%.2f' % weight)
#格式化输出多个
print('age:%d,name:%s' % (age, name))
# 语法 f'{变量名称}'
print(f'name:{name},age:{age}')
#\n 换行 \t 制表符tab
print('hello \n python')
print('hello\tpython')

#八进制
print('age:%o' % age)
#16进制
print('age:%x' % age)
