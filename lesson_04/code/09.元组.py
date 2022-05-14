# 元组 tuple
# 元组为不可变序列，其余都跟列表一致

# 创建元组
my_tuple = (10, 20, 30, 40)
print(type(my_tuple))

# # 元组解包
# a, b, c, d = my_tuple
# print("a=", a)
# print("b=", b)
# print("c=", c)
# print("d=", d)

# 变量数量应与元素数量一致
# 或者变量前添加*表示剩余所有元素，但不能同时出现两个或以上的*
a, b, *c = my_tuple
*a, b, c = my_tuple
a, *b, *c = my_tuple
print("a=", a)
print("b=", b)
print("c=", c)

# # 使用解包交换变量
# a = 100
# b = 200
# a, b = b, a
# print("a=", a)
# print("b=", b)
