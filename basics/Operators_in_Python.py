print('#############Arithmetic Operators###########')

a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

print('#############Comparison Operators###########')

x = 10
y = 20

print(x < y)
print(x > y)
print(x <= y)
print (x >= y)

print('#############Equality Operators###########')

a1 = 10
a2 = 15

print(a1 == a2)
print(a1 != a2)

t1 = [1,2,3]
t2 = [1,2,3]
t3 = t1
print(id(t1), id(t2), id(t3))
print(t1 == t2)
print(t1 is t2)
print(t1 is t3)

print('#############Logical Operators###########')

a3 = True
a4 = False

print(a3 and a4)
print(a3 or a4)
print(not a4)

print('#############Bitwise Operators###########')

a5 = True
a6 = False

print(a5 & a6)
print(a5 | a6)
print(a5 ^ a6)

print('#############Shift Operators###########')

s1 = 1
s2 = 2

print(bin(s1), bin(s2))

x1 = s1 << 2
x2 = s2 >> 2

print(bin(x1), bin(x2))

print('#############Ternary Operators###########')

a = 10
b = 15
c = 20 if a > b else 34

print(c)

print('#############Assignment Operators###########')

a = 10
print(a)

