class Cat():
    __age = 20

    # 定义成类方法@classmethod
    @classmethod
    def get_age(cls):
        return cls.__age


# 无@classmethod 类方法不能被类名直接调用
# print(Cat.get_age()) #TypeError: get_age() missing 1 required positional argument: 'self'
print(Cat.get_age()) #添加@classmethod后
cat = Cat()
print(cat.get_age())
