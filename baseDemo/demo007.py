'''
while循环
'''
count = 0
while count <= 10:
    print(count,end=' ')
    count += 1
print('over')

'''
continue:满足条件时，跳过本次循环
break:满足条件时，跳出循环
'''
i = 0
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print(i,end=' ')
print('over')

u = 0
while True:
    print(u,end=' ')
    u += 1
    if u > 10:
        break
print('over')

'''
无限循环
'''
v0 = 1
v1 = 0
while v0 == 1:
    v1 += 1
    print('执行',v1,'次循环')
print('over')