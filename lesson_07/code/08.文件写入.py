file_name = "dir\\images.png"

with open(file_name, mode="rb") as file_obj:
    name = "new.png"
    with open(name, "wb") as new_obj:
        # 定义每次读取的大小
        chunk = 1024 * 100
        while True:
            # 从已有文件中读取内容
            content = file_obj.read(chunk)
            # 内容为空则退出循环
            if len(content) == 0:
                break
            # 写入新文件
            new_obj.write(content)
