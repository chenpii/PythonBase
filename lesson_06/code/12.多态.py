class A():

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class B():

    def __init__(self, name):
        self._name = name

    def __len__(self):
        return 10

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class C():
    pass


a = A("Tom")
b = B("Jerry")


# 定义一个函数
def say_hello(obj):
    print(obj.name, "hello")


say_hello(a)
say_hello(b)

print(len(b))
