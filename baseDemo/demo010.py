'''
Number，用于存储数值类型
'''
n1 = 1.12
n2 = 2.22
print(n1,n2)
# del n1,n2
# if n1 == 1:
#     print(n1)
# elif n2 == 2:
#     print(n2)
# else:
#     print('over')
n1 = int(n1)
print(n1)
n1 = complex(n1,1)
print(n1)
'''
math、cmath模块
math：浮点数数学运算
cmath：负数数学运算
'''
import math
import cmath
print(dir(math),'\n',dir(cmath))
n1 = 1
n2 = 1.1
n3 = 10
n4 = -1
n5 = -1.1
l = [n1,n2,n3,n4,n5]
for i in range(len(l)):
    if i < 5:
        print('序列',i,'绝对值是',abs(l[i]))
    else:
        print('over')
        break

