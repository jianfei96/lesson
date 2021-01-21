# 多态：同一种行为（方法）不同对象的表现形态（执行不同的功能）
"""
1 定义父类提供公共的方法
2 定义不同子类继承父类，重写功能方法4
3 创建多个子类对象执行方法
"""

# 1 通用模板
class Animal():
    def eat(self):
        pass

# 2 定义子类
class Dog(Animal):
    def eat(self):
        print("吃狗粮")


class Cat(Animal):
    def eat(self):
        print("吃猫粮")

class Person():
    def eat(self,obj):
        obj.eat()

# 3 创建对象
dog = Dog()
dog.eat()
cat = Cat()
cat.eat()

person = Person()
person.eat(dog)
person.eat(cat)