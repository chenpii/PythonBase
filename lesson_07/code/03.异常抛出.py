class MyException(Exception):
    pass

def add(a, b):
    # 如果a和b中有负数，就向调用处抛异常
    if a < 0 or b < 0:
        #raise用于向外抛出异常
        # 目的：告诉调用者这里调用出现异常，希望调用者自己处理一下
        raise MyException("两个参数中不能有负数")
    r = a + b
    return r


print(add(-123, 456))
