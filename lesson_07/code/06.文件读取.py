file_name = "dir\\demo.txt"

# # 普通读取
# try:
#     with open(file_name, encoding="utf-8") as file_obj:
#         # 读取文件
#         content = file_obj.read(6)
#         print(content)
#         print(len(content))
# except FileNotFoundError as e:
#     print(file_name, "不存在")

# 读取大文件

try:
    with open(file_name, encoding="utf-8") as file_obj:
        # 定义变量指定每次读取的大小
        chunk = 100
        # 定义变量保存文件内容
        file_context = ""
        # 循环读取
        while True:
            # 读取指定大小内容
            content = file_obj.read(chunk)

            # 检查是否读取到了内容
            if len(content) == 0:
                break
            file_context += content

except FileNotFoundError as e:
    print(file_name, "不存在")
print(file_context)
