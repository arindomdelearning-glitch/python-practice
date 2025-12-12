A = 10
print(A)

Test = 20
TEST = 30
test = 40
print (Test, TEST, test)

test123 = 1
print(test123)

_test = 4
print(_test)

__test = 5
print(__test);

__test__ = 6
print(__test__);

import keyword
print(keyword.kwlist)


xxxxxxxxxxxxxxxxxxxxxxxxxxx = 12
print(xxxxxxxxxxxxxxxxxxxxxxxxxxx)

print('##########Python Data type##############')

print('##########decimal Data type##############')

a = 12
print(a, type(a), id(a))


print('##########Binary Data type##############')
b = 0b111
print(b, type(b), id(b))

print('##########Octal Data type##############')
c = 0o1234
print(c, type(c), id(c))

print('##########hexa decimal Data type##############')
d = 0x7b
print(d, type(d), id(d))

print('##########float Data type##############')
e = 2.35
print(e, type(e), id(e))

f = 1.3e9
print(f, type(f), id(f))

print('##########Complex Data type##############')
g = 2+3j
print(g, type(g), id(g))
print(g.imag, g.real)

print('##########Bool Data type##############')
bool = True
print(bool, type(bool), id(bool))
print(True + True)
print(True + False)

print('##########String Data type##############')
h = 'Test'
print(h, type(h), id(h))
print(h[0], h[-1])

i = 'test_data'
print(i[0:3])
print(i[2:])
print(i[:2])

j = 'testdata'
print(i[0].upper()+j[1:])
print(j[1].upper()+j[1:len(j)-1]+j[-1].upper())

print('##########Type casting##############')

floattoint = int(12.46)
print(floattoint)

inttofloat = float(12)
print(inttofloat)

inttostr = str(12)
print(inttostr)

inttocomplex = complex(2)
print(inttocomplex)

floattocomplex2 = complex(2.3)
print(floattocomplex2)

print('##########List data type##############')

list = [1,2,3.4,'test']
print(list)
print(type(list))
print(list[0], list[1], list[-1])

list.append(50)
print(list)

list.remove(2)
print(list)

print('##########Tuple data type##############')

tuple1 = (1,2,3,4,'test1')
print(tuple1)
print(type(tuple1))
print(tuple1[0], tuple1[1], tuple1[-1])

tuple2 =()
print(tuple2)
print(type(tuple2))

print('##########Set data type##############')

set1 = {1,2,3,4}
print(set1)
print(type(set1))

set1.add(3)
print(set1)

set1.remove(4)
print(set1)

fs = frozenset(set1)
print(fs)
print(type(fs))

set1.add(3)
print(fs)

print('##########Dict data type##############')

dict1 = {1:1, 2:12, 3:'Test2'}
print(dict1)
print(type(dict1))

dict1[2] = 40
print(dict1)

print('##########Range data type##############')

r = range(1,10,2)
print(type(r))

for x in r:
    print(x)


print('##########Byte data type##############')

b = [1,2,3,4]
byt = bytes(b)
print(byt)
print(type(byt))

b1 = [2,3,6,8]
r = bytearray(b1)
print(r)
print(type(r))