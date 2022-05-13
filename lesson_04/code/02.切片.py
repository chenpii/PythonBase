# 切片
# 通过索引获取子列表
# 语法:列表[起始:结束] 不包括结束位置的元素
#
names = ["tom", "jack", "amy", "bob", "ross"]
subname = names[3:]
print(subname)   # ['bob', 'ross']
subname = names[:3]
print(subname)   # ['tom', 'jack', 'amy']
subname = names[:]
print(subname)   # ['tom', 'jack', 'amy', 'bob', 'ross']

subname = names[3::-1]
print(subname)   # ['bob', 'ross']
subname = names[:3:-1]
print(subname)   # ['tom', 'jack', 'amy']
subname = names[::-1]
print(subname)   # ['tom', 'jack', 'amy', 'bob', 'ross']