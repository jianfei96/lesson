#自定义异常，继承Exception
#Exception是所有异常的父类

class ShortInputError(Exception):#必须继承Exception，否则exceptions must derive from BaseException
    def __init__(self,length,min_len):
        self.length = length
        self.min_len = min_len
    #设置异常的描述信息
    def __str__(self):
        return f'密码长度：{self.length}，不能少于{self.min_len}'

def main():
    try:
        password = input('请输入密码：')
        if len(password) < 3:
            #抛出异常类创建的对象
            raise ShortInputError(len(password),3)
    except Exception as e:
        print(e)
    else:
        print('没有异常，密码长度符合要求')

main()

