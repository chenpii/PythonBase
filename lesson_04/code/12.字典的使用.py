# dict()函数创建字典
my_dict = dict(name="Tom", age=18, sex="man")
print(my_dict, type(my_dict))

# # 双值子序列创建字典
# my_dict = dict([("name", "Tom"), ("age", 18), ("sex", "man")])
# print(my_dict, type(my_dict))

# # 长度
# print(len(my_dict))

# # 是否包含键
# print("name" in my_dict)
# print("name" not in my_dict)

# # 获取值
# print(my_dict.get("name"))
# print(my_dict.get("hight"))

# 修改、添加
# my_dict["name"] = "Jerry"
# print(my_dict)
# my_dict["high"] = 180
# print(my_dict)

# my_dict2 = dict(name="Jerry", rich=50, heigh=180)
# my_dict.update(my_dict2)
# print(my_dict)

# 删除
# # popiteam :删除最后一个
# item=my_dict.popitem()
# print(item)
# print(my_dict)

# # pop 根据key删除
# item = my_dict.pop("name1", "this is default")
# print(item)
# print(my_dict)

# # clear()
# my_dict.clear()
# print(my_dict)

# 浅复制
dict = {"data": {'name': 'Tom', 'age': 18, 'sex': 'man'}, "AAA": 123}
dict2 = dict.copy()
dict2["data"]["name"] = "Jack"
print(dict)
print(dict2)
