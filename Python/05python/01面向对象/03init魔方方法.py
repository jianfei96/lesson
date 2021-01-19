class Washer():
    def __init__(self):
        self.width = 100
        self.height = 100

    def info(self):
        print(f'class height:{self.height}')
        print(f'class width:{self.width}')


wash = Washer()
wash.info()
