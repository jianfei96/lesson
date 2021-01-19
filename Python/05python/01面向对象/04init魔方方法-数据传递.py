class Washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def info(self):
        print(f'class height:{self.height}')
        print(f'class width:{self.width}')


wash = Washer(200,300)
wash.info()
wash1 = Washer(height=999,width=998)
wash1.info()