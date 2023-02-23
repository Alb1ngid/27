# 1 наследование
# 2 полиморфизм

class Person:
    people = 'people'
    head = 1

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def prints(self):
        print(f'мое имя {self.name} мой возраст {self.age}')


per1 = Person('Ислам', 10)


# per1.prints()
# per1 = Person('Ислам', 10)
# per1.prints()
# per1 = Person('Ислам', 10)
# per1.prints()
# per1 = Person('Ислам', 10)
# per1.prints()


class Person2(Person):

    people = 'Monster in programing'

    def __init__(self, name, age, super_power):
        super().__init__(name, age)
        Person.__init__(self, name, age)
        self.power = super_power

    def prints(self):
        print(f'мое имя {self.name} мой возраст {self.age} и я умею {self.power}')

    def x(self):
        # super().prints()
        Person.prints(self)


per2 = Person2('Болотбек', 2, 'летать')
per2.prints()
per1.prints()
per2.x()
# print(per1.people, per2.people)


