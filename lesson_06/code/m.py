# 在模块中定义变量
a = 10
b = 20


# 在模块中定义函数
def test():
    print("test")


def test2():
    print("test2")


# 在模块中定义类
class Person():
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return "Person[name=%s ,age=%d]" % (self._name, self._age)

    def __lt__(self, other):
        return self._age < other._age


if __name__ == '__main__':
    p = Person("Jerry", 18)
    print(p)
