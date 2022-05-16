file_name = "dir\\demo.txt"
with open(file_name, mode="rb") as file_obj:
    # seek() 修改当前读取的位置
    file_obj.seek(80, 0) # 从头开始的第80
    file_obj.seek(70, 1) # 从当前位置开始后的第70
    file_obj.seek(-1, 2) # 获取倒数10个

    # tell() 查看当前读取的位置
    print("当前读取到了-->", file_obj.tell())
