'''
变量赋值
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）
'''
#整型
counter = 100
#浮点型
miles = 100.0
#字符串
name = "goodman"
print(counter)
print(miles)
print(name)

#多变量赋值
a = b = c = 10
d,e,f = 1,2.0,"badman"
print(a,b,c)
print(d,e,f)

'''
数字类型
int（有符号整型）
long（长整型，可代表八进制或十六进制）
float（浮点型）
complex（复数）
'''
v1 = 1
v2 = 10
print(v1,v2)
del v1
# print(v1,v2)  取消引用，无效
del v2
# print(v1,v2)

v3 = 10
v4 = -1000
v5 = 0x69
v6 = complex(10,1)
print(v3,v4,v5,v6)

'''
String:字符串
'''
s0 = "it's a str"
print(s0)
s1 = s0[0]
s2 = s0[7:10]
s3 = s0[0:]
s4 = s0 * 2
s5 = s0 + " and a test"
print('s1:'+s1)
print('s2:'+s2)
print('s3:'+s3)
print('s4:'+s4)
print('s5:'+s5)

'''
list:列表
'''
l0 = [a,s0,'a','b','c','d']
print(l0)
print(l0[0])
print(l0[1:3])
print(l0[2:])
print(l0*2)
print(l0+l0)

'''
tuple:元祖
类似list，不可二次赋值，相当于只读列表
'''
t0 = ('a',a,10.1,l0[0])
print(t0)
print(t0[0])
print(t0[0:2])
print(t0[2:])
print(t0*3)
print(t0+t0)
# t0[0] = 'b'  不支持赋值
# print(t0)

'''
dictionary:字典
无需对象集合，字典中的元素需要通过键来存取，不通过偏移存取
'''
dict0 = {}
print(dict0)
dict0['one'] = a
print(dict0)
dict0[2] = s0
print(dict0)
print(dict0['one'])
print(dict0[2])
print(dict0.keys())
print(dict0.values())

'''
数据类型转换
'''
i0 = 100.0
print(i0)
i1 = int(i0)
print(i1)
i2 = float(i0)
print(i2)
i3 = complex(i0,1)
print(i3)
i4 = str(i0) + ' str test'
print(i4)
i5 = repr(i0) + '表达式'
print(i5)
# i6 = eval('test000')
# print(i6)
i7 = tuple(s0)
print(i7)
i8 = list(s0)
print('列表：')
print(i8)
i9 = set(s0)
print(i9)
