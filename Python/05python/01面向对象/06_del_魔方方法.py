class Washer(object): #所有类默认继承object类，不写object也可以
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def __str__(self):
        return f'height:{self.height},width:{self.width}'

    def __del__(self):
        print('对象被解释器释放！')

#程序执行完成，事情内存会被自动释放
wash = Washer(100,200)

