import os
import sys
from pprint import pprint

# 当前命令的参数
sys.argv
print(sys.argv)

# 引入的模块
pprint(sys.modules)
# 模块搜索路径
pprint(sys.path)
# 运行的平台
pprint(sys.platform)

# 系统环境变量
pprint(os.environ)
# 执行操作系统的名字
os.system("dir")
os.system("notepad")
