class A(object):
    def test(self):
        print("AAA")


class B(object):
    def test(self):
        print("BBB")


class C(B, A):
    def test2(self):
        print("CCC")


print(C.__bases__)
c = C()
c.test()
