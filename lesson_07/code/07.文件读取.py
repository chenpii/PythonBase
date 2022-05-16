from pprint import pprint

file_name = "dir\\demo02.txt"

try:
    with open(file_name, encoding="utf-8") as file_obj:
        # read
        # print(file_obj.read())
        # # readline
        # print(file_obj.readline())
        # print(file_obj.readline())
        # list = file_obj.readlines()
        # pprint(list)
        # pprint(list[0])

        # for循环
        for t in file_obj:
            print(t)

except FileNotFoundError as e:
    print(file_name, "不存在")


