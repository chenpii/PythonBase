# # 使用_属性名 来表示私有属性
# class Dog():
#
#     def __init__(self, name: str):
#         self._name = name
#
#     def set_name(self, name: str):
#         self._name = name
#
#     def get_name(self):
#         return self._name
#
#
# d1 = Dog("旺财")
# print(d1.get_name())
# d1._Dog__name = "小白"
# print(d1.get_name())


class Dog():

    def __init__(self, name: str):
        self._name = name

    # property装饰器,用来将一个get方法，转换成对象的属性
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name


d1 = Dog("旺财")
print(d1.name)
d1.name = "小白"
print(d1.name)
