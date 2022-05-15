class A():

    def __init__(self):
        self.name = 'A类'

    # 在对象被回收之前自动调用
    def __del__(self):
        print("A() 对象被删除了~", self)



a = A()
print(a.name)
a = None