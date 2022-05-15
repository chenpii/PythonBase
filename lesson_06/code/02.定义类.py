class Person():
    # name = ""

    #  构造方法
    def __init__(self, name):
        print("调用__init__方法")
        self.name = name

    def say_hello(self):
        print("你好我是 %s" % self.name)


p1 = Person("Tom")


