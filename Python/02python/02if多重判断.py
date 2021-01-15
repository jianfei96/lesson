age = input('请输入年龄：')
age = int(age)
if 17<=age<30:
    print(f'成年人{age}')
elif 40>= age >=30:
    print(f'青年人{age}')
elif 40 < age <60:
    print(f'中年人{age}')
elif age >=60:
    print(f'老年人{age}') 
else:
    print(f'未成年人{age}')
