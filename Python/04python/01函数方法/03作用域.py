c = 100
def method(a):
    global b #声明全局变量
    b = 10 #赋值，必须分开

method(1) #函数被调用才会执行
print(b)
print(c)