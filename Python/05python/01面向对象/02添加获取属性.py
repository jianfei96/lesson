class Washer():
    def wash(self):
        print("洗衣服")

    def info(self):
        print(f'class height:{self.height}')
        print(f'class width:{self.width}')


wash = Washer()
# 对象.属性 = 值
wash.height = 100
wash.width = 100

print(f'height:{wash.height}')
print(f'width:{wash.width}')
wash.info()
