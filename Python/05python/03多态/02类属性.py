# 类属性：属性定义在类中 实例对象属性：定义在__init__魔方方法中

class Cat():
    age = 18


# 类属性访问格式：类名.属性
print(Cat.age)

# 创建对象： 对象.类属性
cat = Cat()
print(cat.age)

cat.age = 20
print(cat.age)  # 通过对象访问的类属性被修改
print(Cat.age)  # 属于类的类属性通过类修改
Cat.age = 50
print(Cat.age) 
cat = Cat()
print(cat.age)