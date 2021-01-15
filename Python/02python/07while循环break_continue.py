'''
break 满足条件直接退出循环
continue 跳过本次循环
'''

num = input('请输入：')
num = int(num)

while num <=5:
    num += 1
    if num == 3:
        #break
        continue
    print(f'num:{num}')
    
else:
    print('没有循环')