class Person():
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return "Person[name=%s ,age=%d]" % (self._name, self._age)

    def __lt__(self, other):
        return self._age < other._age


p1 = Person("Tom", 25)
p2 = Person("Jerry", 23)
print(p1)
print(p2)
print(p1 < p2)
print(p2 < p1)
