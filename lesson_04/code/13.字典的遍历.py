# 字典的遍历
# keys() 返回所有的key
my_dict = dict(name="Tom", age=18, sex="man")
print(my_dict.keys())

# # 通过所有的key遍历字典
# for key in my_dict.keys():
#     print(key, "=", my_dict[key])

# values() 获取所有的值
print(my_dict.values())

# items() 返回字典所有的项 ,格式为双值子序列
print(my_dict.items())
for k, v in my_dict.items():
    print(k, "=", v)
