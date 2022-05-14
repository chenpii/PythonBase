# 集合
# # 使用{}来创建集合
s = {10, 3, 5, 1, 2, 1, 8}
# print(s, type(s))

# # 使用set()创建集合
# # 将序列和字典转换为集合
# s = set([1, 2, 3, 4, 5, 1, 1, 3])
# print(s)
# s = set("hello")
# print(s)
# s = set({"name": "Tom", "age": 18, "sex": "man"}) # 使用set转换字典，只会保存键
# print(s)

# # 长度 len()
# print(len(s))

# # 增加 add()
# s.add(88)
# print(s)

# # update()
s2 = set("abc")
s.update(s2)
s.update([99, 100])
s.update({"name": "Tom"})
print(s)

# 删除 pop() 随机删除
# s.pop()
# print(s)

# remove()
s.remove(99)
print(s)
