def method():
    return 1, 2, 3

date = method()
a, b, c = method()
print(date)
print(f'a:{a} b:{b} c:{c}')

def method2():
    return {'name': 'tom','age':30}

date2 = method2()
print(date2)