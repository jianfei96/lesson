class Animal():
    def __init__(self):
        self.eat = 'eat'
    def run(self):
        print(f'{self.eat} run')

class Dog():
    def __init__(self):
        self.eat = 'dog eat'
    def run(self):
        print(f'{self.eat} run')

class OtherDog(Animal,Dog):#属性和方法相同时，优先访问第一个父类（子类没有定义相同的属性和方法名）
    pass #没有会报错

otherdog = OtherDog()
print(otherdog.eat)
otherdog.run()