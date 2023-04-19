'''
算数运算符
'''
a = 10
b = 30
print('a+b=',a+b)
print('a-b=',a-b)
c = round(a/b,2)
print('a/b=',c,'（保留两位小数）')
print('a%b=',a%b,'（取余）')
print('b的a次方=',b**a)
print('a//b=',a//b,'（取整）')

'''
比较运算符
'''
a = 10
b = 20
if a == b:
    print('a等于b')
else:
    print('a不等于b')

if a != b:
    print('a不等于b')
else:
    print('a等于b')

if a >= b:
    print('a大于等于b')
else:
    print('a小于b')

if a <= b:
    print('a小于等于b')
else:
    print('a大于b')

'''
赋值运算符
'''
a = 10
b = 100
c = a + b
print('c=a+b=',c)
d =  20
d += c
print('d=d+c=',d)
e = 30
e -= d
print('e=e-d=',e)
f = 2
f *= a
print('f=f*a=',f)
g = 10
g /= f
print('g=g/f=',g)
h = 31.1
h %= a
h = round(h,0)
print('h=h%g=',h)
i = 2
a = 2
i **= a
print('i=i**a=',i)
j = 31
j //= a
print('j=j//a=',j)

'''
位运算符
'''
a = 60 #二进制：0011 1100
b = 13 #二进制：0000 1101
print('a&b=',a&b,'位与运算符')
print('a|b=',a|b,'位或运算符')
print('a^b=',a^b,'位异或运算符')
print('~a=',~a,'位取反运算符')
print('a<<2=',a<<2,'左移动运算符') #1111 0000 十进制：2**4+2**5+2**6+2**7=16+32+64+128=240
print('a<<3=',a<<3,'左移动运算符') #0001 1110 0000 十进制：2**5+2**6+2**7+2**8=32+64+128+256=480
print('a>>2=',a>>2,'右移动运算符') #0000 1111 十进制：2**0+2**1+2**2+2**3=1+2+4+8=15
print('a>>3=',a>>3,'右移动运算符') #0000 0111 十进制：2**0+2**1+2**2=1+2+4=7 溢出部分舍弃

'''
逻辑运算符
'''
a = 10
b = 20
c = 0
print('a and b = ',a and b) #布尔与,相同取相同值，不同取后值
print('b and a = ',b and a)
print('a and a = ',a and a)
print('a or b = ',a or b) #布尔或，前值不为0取前值，否则取后值
print('b or a = ',b or a)
print('a or a = ',a or a)
print('c or b = ',c or b)
print('not(a and b)=',not(a and b)) #布尔非，相同取true，不同取false

'''
成员运算符
'''
a = 10
b = 20
l0 = [10,9,8,7,6,5,4,3,2,1,0]
l1 = [1,2]
s0 = '1'
s1 = '110'
s2 = '220'
t0 = 1
t1 = ('1',1,[1])
print('l1 in l0 =',l1 in l0)
print('l1 in l1 =',l1 in l1)
print('a in l0 =',a in l0)
print('b in l0 =',b in l0)
print('a not in l0 =',a not in l0)
print('b not in l0 =',b not in l0)
print('s0 in s1 =',s0 in s1)
print('s0 in s2 =',s0 in s2)
print('t0 in t1 =',t0 in t1)
print('s0 in t1 =',s0 in t1)

'''
身份运算符
'''
a = 10
b = 20
c = 20
print('a is b =',a is b)
print('c is b =',c is b)
print('a is not b =',a is not b)

'''
运算符优先级次序
0：**
1：~
2：* / % //
3: + -
4: << >>
5: &
6: ^ | 
7: <= < > >=
8: == !=
9: = %= /= //= -= += *= **=
10: is is not
11: in not in
12: not and or
'''
a = 10
b = 2
c = 3
d = 4
e = 5
print('a ** b - c | d =',a ** b - c | d)