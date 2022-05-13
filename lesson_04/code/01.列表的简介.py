# 创建列表
my_list = []  # 创建一个空列表
# print(my_list, type(my_list))

# my_list = [10]  # 创建一个只包含1个元素的列表
# print(my_list)

# my_list = [10, 20, 30, 40, 50]  # 创建一个包含5个元素的列表
# print(my_list)

# 列表中可以保存任意的对象
# my_list = [10, 2.2, "33", True, None]
# print(my_list)

my_list = [10, 20, 30, 40, 50]
print(my_list[-1])
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
