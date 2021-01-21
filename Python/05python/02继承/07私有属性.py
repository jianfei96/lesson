# __私有方法，__私有属性:
# 子类无法访问父类中的私有属性，父类本身也访问不到
# 子类无法访问父类中的私有方法，父类本身也访问不到

# 属性和方法相同时，优先访问第一个父类（子类没有定义相同的属性和方法名）
class OtherDog():
    # 重写：子类会重写父类中相同的属性名值和相同方法
    def __init__(self):
        self.eat = 'otherdog eat'
        self.__age = 10

    def run(self):
        print(f'{self.eat} otherdog run')

    def __sleep(self):
        print(f'sleep')

    def get_age(self):
        return self.__age

    def set_age(self, age):  # 需要定义变量
        self.__age = age


class Other(OtherDog):
    pass


other = Other()
# print(other.__age) #AttributeError: 'Other' object has no attribute '__age'
# other.__sleep() #AttributeError: 'Other' object has no attribute '__sleep'
print(other.get_age())
other.set_age(30)
print(other.get_age())

otherdog = OtherDog()
# print(otherdog.__age) #AttributeError: 'OtherDog' object has no attribute '__age'
# otherdog.__sleep() #AttributeError: 'OtherDog' object has no attribute '__sleep'
