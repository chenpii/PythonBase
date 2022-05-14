names = ["Bob", "Jack", "Jerry", "Tom"]
names[1] = "hello"
print(names)

names[0:2] = ["hello", "world"]
print(names)

del names[0:2]
print(names)

str = "hello"
s = list(str)
del s[0]
str2 = str(s)
print(str2)
