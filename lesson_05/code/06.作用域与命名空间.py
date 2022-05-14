# 作用域
# 全局作用域和函数作用域
#
# a = 20
#
# # 如果希望在函数内部修改全局变量，需要使用global关键字
#
# def fn():
#     global a
#     a = 10
#     print("函数内部a=", a)
#
#
# fn()
# print("函数外部a=", a)

# 命名空间
a = 100
scope = locals()  # 当前命名空间
print(scope)


def fn4():
    a = 10
    scope = locals()  # 函数内部命名空间
    print(scope)
    global_scope = globals()  # 全局命名空间
    print(global_scope)


fn4()
