# 3 инкапсуляция

# публичный
# защищенный _
# скрытый __

# import lesson2
# from lesson2 import *

class Cat:
    xвост = True

    def __init__(self, name, age):
        self._name = name
        self.__age = age

    @property
    def name(self):
        return (self._name,self.__age)
    @name.setter
    def name(self, name,age):
        self._name = name
        self.__age =age

    def __may(self):
        print(self._name, 'мяукает')

    def __str__(self):
        return f'name is {self._name}\n' \
               f'age is {self.__age}'

    def __len__(self):
        return len(self._name)

    def _x2(self):
        self.__age *= 9
        print(self)

    def x(self):
        self._x2()


print()
# # cat = Cat('Beka', 4)
# # cat.name = 'qwertyu'
# # print(cat, cat.name)
# # # cat.may()
# # cat2 = Cat('Бегимай', 4)
# # cat2._name = 'Бегайым'
# # print(cat2)
# # cat2.x()
# # cat2._x2()
# # cat2.__age = 'q'
# # print(cat2)
# # print(dir(Cat))
# # cat2._Cat__age = 9
# # print(cat2._Cat__age)
# # cat2._Cat__may()
#
cat3 = Cat('Эрик', 3)
# # cat3.set_name('Барсик')
# # cat3.name = ''
#
# print(cat3.name)
# d=9
# Cat.x(d)
print(cat3._Cat__age)
print(cat3._Cat__may())


print(cat3._name)
#print(cat3.__age)
