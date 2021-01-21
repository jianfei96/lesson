"""
try:
    pass 存在异常的代码
except expression as identifier: 异常类型
    pass 异常出现时执行

"""
try:
    # 1 + '1'
    # 1 / 0
    open('1.txt','r')
except (FileNotFoundError,ZeroDivisionError,TypeError) as e: #捕获指定异常
    print(e)
