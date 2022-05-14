# 返回值
# def sum(*a):
#     result = 0
#     # 遍历元组
#     for n in a:
#         result += n
#     return result
#
#
# print(sum(123, 456, 789))


# 返回值是函数
def fn():
    def fn2():
        print("hello")

    return fn2()


r = fn()
print(fn)