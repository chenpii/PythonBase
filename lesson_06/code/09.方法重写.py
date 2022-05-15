class A():
    def test(self):
        print("AAA")


class B(A):
    def test(self):
        print("BBB")


class C(B):
    def test(self):
        print("CCC")


c = C()
c.test()
