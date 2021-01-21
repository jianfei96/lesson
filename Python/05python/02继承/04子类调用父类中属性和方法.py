class Animal():
    def __init__(self):
        self.eat = 'eat'
    def run(self):
        print(f'{self.eat} run')

class Dog():
    def __init__(self):
        self.eat = 'dog eat'
    def run(self):
        print(f'{self.eat} dog run')

#属性和方法相同时，优先访问第一个父类（子类没有定义相同的属性和方法名）
class OtherDog(Animal,Dog):
    #重写：子类会重写父类中相同的属性名值和相同方法
    def __init__(self):
        self.eat = 'otherdog eat'
    def run(self):
        print(f'{self.eat} otherdog run')
    def animal_method(self):
        Animal.__init__(self)
        Animal.run(self)
        #print(Animal.eat)
    def dog_method(self):
        Dog.__init__(self)
        Dog.run(self)


otherdog = OtherDog()
#print(otherdog.eat)
otherdog.run()
otherdog.animal_method()
otherdog.dog_method()