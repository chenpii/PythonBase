class Person():
    name = ""

    def say_hello(self):
        print("你好我是 %s" % self.name)


p1 = Person()
p2 = Person()
p1.name = "Tom"
p2.name = "Jerry"
p1.say_hello()