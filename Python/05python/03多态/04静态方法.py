class Cat():
    @staticmethod
    def static():
        print('static')

    def info(self):
        print('self')


cat = Cat()
# cat.static()  # TypeError: info_print() takes 0 positional arguments but 1 was given
cat.static()  # add @staticmethod
cat.info()

Cat.static()  # 静态方法可以通过对象和类名调用，无需传递实例对象，类对象
# Cat.info()  # 无法通过类名调用
