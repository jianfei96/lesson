def print_method(a, b):
    print(a+b)


print_method(1, 2)
print_method('a', 'b')


def add(a, b):
    """
    相加
    :param a: 参数1
    :param b: 参数2
    :return: 返回相加结果
    """
    #方法可以嵌套，定义方法中可以再去调用
    return a+b


result = add(1, 2)
print(result)

help(add)