# __str__ 打印对象时自动执行

class Washer():
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def __str__(self):
        return f'height:{self.height},width:{self.width}'

wash = Washer(100,200)
print(wash)