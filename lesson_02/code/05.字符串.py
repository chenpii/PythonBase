# 【字符串】
# 用来表示一段文本信息，在python中需要使用引号。可以是单引号，也可以是双引号。
s = 'hello'
s = "hello"

# 相同的引号之间不能嵌套
# s="子曰："学而时习之，不亦乐乎""
s = "子曰：'学而时习之，不亦乐乎'"

# 【长字符串】
# 单引号和双引号无法跨行使用
s = '锄禾日当午，\
汗滴禾下土，\
谁知盘中餐，\
粒粒皆辛苦'

# 三重引号
s = '''锄禾日当午，
汗滴禾下土，
谁知盘中餐，
粒粒皆辛苦。
'''
# 转移字符

s='\u2250'
print(s)
