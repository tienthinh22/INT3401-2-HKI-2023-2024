print(1 + 1)
print(2 * 3)
print(1 == 0)
print(not (1 == 0))
print(~(1 == 0))
print((2 == 2) and (2 == 3))
print((2 == 2) or (2 == 3))
print("artificial" + "intelligence")
print("artificial".upper())
print("HELP".lower())
print(len("Help"))
print()

s = "hello world"
print(s)
print(s.upper())
len(s.upper())
num = 8.0
num += 2.5
print(num)

s = "abc"
print(dir(s))
help(s.find)
print(s.find('b'))

import copy

x = (1, 1)

y = copy.copy((1, 1))

print(id(x))
print(id(y))

#input set
set1 = {1, 2, 3, 4, 5}
 
x = iter(set1)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(set1)
#prints first item

print(dir(tuple))
help(tuple.__getstate__)
print(dir(int))
help(int.__getstate__)