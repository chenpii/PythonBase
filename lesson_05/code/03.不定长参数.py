# 不定长参数
# 求和
# def sum(*a):
#     result = 0
#     # 遍历元组
#     for n in a:
#         result += n
#     print(result)
#
#
# sum(1, 2)
# sum(5, 15, 25)
# sum(6, 66, 666)

# *与其他形参混合使用
# def fn(a,b,*c):
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)
#
#
# fn(1,2,3,4,5)

# *写前，强制要求传递关键字参数
# def fn(*, a, b, c):
#     print("a=", a)
#     print("b=", b)
#     print("c=", c)
#
# fn(a=1, b=2, c=3)

# *只能接收位置参数，不能接受关键字参数
# def fn(*a):
#     print("a=", a)
#
#
# fn(a=1) # 报错：got an unexpected keyword argument

# **形参可以接收关键字
# 只能有1个，且必须在最后
# def fn(b, c, **a):
#     print("a=", a)
#     print("b=", b)
#     print("c=", c)
#
#
# fn(b=1, d=2, c=3, e=10, f=20)

# 参数的解包
def fn(a, b, c):
    print("a=", a)
    print("b=", b)
    print("c=", c)


t = (10, 20, 30)
fn(*t)

d = {"a": 100, "b": 200, "c": 300}
fn(**d)
