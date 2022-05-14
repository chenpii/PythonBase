# 函数递归

# # 定义阶乘函数
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
#
#
# print(factorial(4))

# 练习1
# 创建一个函数power来为任意数字做幂运算 n**i
# def power(n, i):
#     if i == 1:
#         return n
#     return n * power(n, i - 1)
#
#
# print(power(2, 5))


# 练习2
# 创建一个函数，用来检查一个任意的字符串是否是回文字符串，如果是返回True，否则返回False
# 回文字符串：字符串从前往后和从从后往前都是一样的，abcba
def check(str):
    # 字符串长度小于2，一定是回文
    if (len(str) < 2):
        return True
    # 第一个字符串跟最后一个不一样，不是回文
    if (str[0] != str[-1]):
        return False
    # 递归检查第二个到倒数第二个的子字符是否是回文
    return check(str[1:-1])


print(check("abccba"))
