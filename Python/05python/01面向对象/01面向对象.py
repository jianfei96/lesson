# 类：创建一类对象的事物的模板
'''
类的格式：
class 类名():
    代码

创建对象：
    对象=类名
'''
class Washer():
    def wash(self):
        print("洗衣服")
        print(self)

wash = Washer()
wash1 = Washer()
print(id(wash))
wash.wash()
wash1.wash()
print(wash)
print(wash1)
