# 函数的参数
# 指定默认值
def fn(a=5, b=10):
    print("a=", a)
    print("b=", b)


fn(100, 200)
fn(b=222, a=111)


def fn(a=5, b=10, c=15):
    print("a=", a)
    print("b=", b)
    print("c=", c)


fn(3, 6, c=9)
