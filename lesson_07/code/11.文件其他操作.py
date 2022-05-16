import os
from pprint import pprint

# r = os.listdir()
# pprint(r)
#
r = os.getcwd()
# pprint(r)

# 修改当前路径
# os.chdir("..")

# 增删目录
# os.mkdir("testdir")
# os.rmdir("testdir")

# 创建文件
# open("aa.txt","w")
# 删除文件
# os.remove("aa.txt")
# 重命名/移动
os.rename("aa.txt", "bb.txt")

pprint(r)
