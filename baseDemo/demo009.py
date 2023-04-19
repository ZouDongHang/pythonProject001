'''
break语句,满足条件，跳出当前层循环
'''
for l in 'python':
    if l == 'h':
       break
    print('字母为:',l)

i = 10
while i > 0:
    print('变量为:',i)
    i -= 1
    if i == 1:
        break
print('over')

'''
continue语句，满足条件，跳过当前层循环的剩余部分
'''
for l in 'python':
    if l == 'o':
        continue
    print('字母为:',l)
print('over')

v = 10
while v > 0:
    v -= 1
    if v == 5 or v == 7:
        continue
    print('变量为:', v)
print('over')

'''
pass语句，空语句，保持结构完整性，不做任何事情
'''
for i in 'python':
    if i == 'o':
        pass
        print('pass块')
    print('字母为:',i)
print('over')
