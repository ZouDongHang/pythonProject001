'''
for循环
'''
l = [1,2,3,4,5]
for l1 in l:
    print('当前为:',l1)
print('over')

l = [1,2,3,4,5]
for l in l:
    print('当前为:',l)
print('over')

'''
通过序列索引遍历
'''
l = ['零','一','二','三','四','五']
print(len(l))
print(range(len(l)))
print(l.index('一'))
for index in range(len(l)): #range()返回序列索引数 len()返回序列长度
    print('当前为:',l[index])
print('over')

'''
循环使用else语句
'''
for num in range(10,20):
    for i in range(2,num):
        if num % i == 0:
            j = num/i
            print('%d = %d * %d'%(num,i,j))
            break
    else:
        print('%d 是质数'%num)

'''
嵌套循环
'''
i = 2
while i < 100:
    j = 2
    while j <= (i / j): #
        if not (i % j):
            break
        j += 1
    if j > (i / j):
        print('%d 是素数'%i)
    i += 1
print('over')