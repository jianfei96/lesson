list1 = [1, 1.1, True, 'string', [2, 'string']]

i = 0
while i < len(list1):
    print(list1[i])
    i += 1

for i in range(len(list1)):
    print(list1[i])

for i in list1:
    print(i)