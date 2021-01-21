"""
try:
    pass 存在异常的代码
except expression as identifier: 异常类型
    pass 异常出现时执行

"""
try:
    f = open('1.txt','r')
    print('test') #出现异常后中断，执行except
except Exception as e: #捕获所有异常信息
    print(e)
else:
    print('没有异常时执行')