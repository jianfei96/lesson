while 1:
    age = input('请输入年龄：')
    try:
        age = int(age)
        pass
    except:
        print('请输入正确年龄:')
        age = 0
        continue
    if age <0 or age >100:
        print('请输入正确年龄:')
        age = 0
        continue
    elif 17 <= age < 30:
        print(f'成年人{age}')
    elif 40 >= age >= 30:
        print(f'青年人{age}')
    elif 40 < age < 60:
        print(f'中年人{age}')
    elif age >= 60:
        print(f'老年人{age}')

    else:
        print(f'未成年人{age}')

