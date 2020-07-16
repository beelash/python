##################
#два вида создания и использования классов в коде
class Person:
        name = "ivan"
        age = 10
##################
        def __init__(self, name, age):
            self.name = name
            self.age = age
ivan = Person("Вася", 32)
#ivan.set ("Ivan", 32)
print(ivan.name + " " + str(ivan.age))
##################
#vlad = Person()
#vlad.name = 'Vlad'
#vlad.age = 25
#print(vlad.name + ' ' + str(vlad.age))