# 闭包
# 通过闭包可以创建一些只有当前函数能访问的变量
# 可以将一些私有的数据藏到闭包中

def fn():
    a = 10

    # 函数内部定义一个函数
    def inner():
        print("我是内部函数", a)

    return inner


r = fn()
r()


def make_avg():
    nums = []

    def avg(n):
        nums.append(n)
        return sum(nums) / len(nums)

    return avg


averager = make_avg()
print(averager(10))
print(averager(20))
print(averager(30))
