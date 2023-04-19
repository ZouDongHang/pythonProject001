'''
条件语句
'''
a = False
b = 'goodman'
if b == 'goodman':
    a = True
    print(b)
else:
    b = 'badman'
    print(b)

a = False
b = 1
if b == 1:
    a = True
    print(a)
elif b > 1:
    print(a)
elif b < 1:
    print(a)

a = 0
b = 1
c = 2
d = 3
if a > b and c > d:
    print(a,c)
elif a < b and c > d:
    print(b,c)
elif a > b and c < d:
    print(a,d)
elif a < b and c < d:
    print(b,d)

if a > b or c > d:
    print(a,c)
elif a < b or c > d:
    print(b,c)
elif a > b or c < d:
    print(a,d)
elif a < b or c < d:
    print(b,d)