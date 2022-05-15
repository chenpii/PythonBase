# 自定义一个表示狗的类
# 属性：name、age、gender、height
# 方法：eat()、run()

class Dog():

    def __init__(self, name: str, age: int, gender: str, height: int):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def run(self):
        print(self.name, "running")

    def eat(self):
        print(self.name, "eating")


d1 = Dog("旺财", 2, "boy", 8)
d1.run()
d1.eat()
