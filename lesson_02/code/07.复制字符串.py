# 创建变量保存名字
name = 'Tom'

# 使用四种方式来输出 欢迎 xxx 光临
# 拼接
print('欢迎 ' + name + ' 光临')
# 多个参数
print('欢迎', name, '光临')
# 占位符
print('欢迎 %s 光临' % name)
# 格式化字符串
print(f'欢迎 {name} 光临')

# 字符串的复制
# 使用字符串与数字相乘
s = 'abc'
s = s * 2
print(s)
