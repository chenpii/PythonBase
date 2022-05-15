# 定义类
class A(object):
    count = 0

    # 类属性：直接在类中定义
    #   可以通过类或者类的实例访问到
    #   只能通过类对象来修改，无法通过实例对象修改

    def __init__(self):
        self.name = '孙悟空'
        # 实例属性：通过实例对象添加的属性
        #   只能通过实例对象来访问和修改，类对象无法访问修改

    def test(self):
        # 实例方法：在类中定义，第一个参数是self的方法都是实例方法
        #   当通过实例调用时，会将调用对象作为self传入
        #   当通过类调用时，不会自动传递self,此时必须手动传递self
        print("这是test=，实例方法")

    # 类方法：类内部使用@classmethod修饰方法
    @classmethod
    def test_2(cls):
        print("这是test2，类方法")

    # 静态方法：使用@staticmethod修饰的方法
    # 不需要指定参数，类和实例都可以去调用
    # 基本上是一个和当前类无关的方法，只是一个保存到当前类中的函数。
    @staticmethod
    def test_3():
        print("这是test_3,静态方法")


a = A()
#属性
print("A,", A.count)
print("a,", a.count)
# print("A,",A.name) # 报错，无法访问
print("a,", a.name)
#实例方法
a.test()
# A.test() # 报错，不会自动传self
A.test(a)  # 等价于 a.test()
#类方法
A.test_2()
a.test_2()
#静态方法
A.test_3()
a.test_3()