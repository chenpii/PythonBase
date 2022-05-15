class Animal():
    def run(self):
        print("动物跑")

    def sleep(self):
        print("动物睡觉")


class Dog(Animal):
    def bark(self):
        print("汪汪汪")


class Husky(Dog):
    def komatik(self):
        print("哈士奇拉雪橇")


h1 = Husky()
h1.run()
h1.sleep()
h1.bark()
h1.komatik()
