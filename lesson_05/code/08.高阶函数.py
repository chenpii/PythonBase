# 高阶函数
# 接收1个或多个函数作为参数 或 将函数作为返回值返回

ls = [1, 2, 3.4, 5, 6, 7, 8, 9, 10]


# 定义一个函数用来检查一个任意数是否是偶数
def fn2(i):
    if i % 2 == 0:
        return True
    return False


# 定义一个函数用来检查一个任意数是否大于5
def fn3(i):
    if i > 5:
        return True
    return False


# 定义函数：返回一个子列表
def fn(func, list):
    new_list = []

    for n in list:
        if (func(n)):
            new_list.append(n)

    return new_list


print(fn(fn2, ls))
print(fn(fn3, ls))
print(list(filter(fn2, ls)))

# lombda 匿名函数
ls = [1, 2, 3.4, 5, 6, 7, 8, 9, 10]


# 判断奇偶函数
def fn2(i):
    if i % 2 == 0:
        return True
    return False


# 改造成lombda
lambda i: i % 2 == 0
r = filter(lambda i: i % 2 == 0, ls)
print(list(r))

# map()
ls = [1, 2, 3.4, 5, 6, 7, 8, 9, 10]
r = map(lambda i: i + 1, ls)
print(list(r))

# sort()
ls = ["bb", "aaaa", "c", "ddddddd", "fff"]
ls.sort(key=len)
print(ls)

# sorted()
ls = ["bb", "aaaa", "c", "ddddddd", "fff"]
r = sorted(ls, key=len)
print(ls)
print(r)
