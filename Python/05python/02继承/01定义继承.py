#继承：子类默认继承父类所有属性和方法
'''
class 子类(父类):
    方法
'''

class Father():
    def __init__(self):
        self.age = 40

    def info(self):
        print(f'age:{self.age}')
    def __str__(self):
        return str(self.age)
    def __del__(self):
        print('deleted'+str(self.age))

class Child(Father):
    pass#没有其他代码

child = Child()
child.info()
print(f'age:{child.age}')
print(child)