a_1 = [1, 2, 3, 4]
a_2 = a_1
a_3 = a_1

print(a_1)
print(type(a_1))
print((id(a_1)))
print(a_2)
print(type(a_2))
print(id(a_2))
print(a_3)
print(type(a_3))
print(id(a_3))
if a_1 == a_2:
    print(True)
if a_2 == a_3:
    print(True)
else:
    print(False)

b_1 = [190, 321]
b_2 = [190, 321]
print(b_1)
print(type(b_1))
print((id(b_1)))
print(b_2)
print(type(b_2))
print(id(b_2))

a1 = set(a_1)
a2 = set(a_2)
a3 = set(a_3)
print(a1)
print(type(a1))
print((id(a1)))
print(a2)
print(type(a2))
print(id(a2))
print(a3)
print(type(a3))
print(id(a3))

b1 = tuple(b_1)
b2 = tuple(b_2)
print(b1)
print(type(b1))
print((id(b1)))
print(b2)
print(type(b2))
print(id(b2))
