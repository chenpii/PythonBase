# with as 语句
file_name = "dir\\demo1.txt"

try:
    with open(file_name) as file_obj:
        print(file_obj.read())
except FileNotFoundError as e:
    print(file_name, "不存在")