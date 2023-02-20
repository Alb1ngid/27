class A:
    def __init__(self, name):
        self.name = name

    def p(self=True):
        print('это функция А')


class B(A): ...


# def p(self=True):
#     print('это функция Б')


class C:
    def __init__(self, age):
        self.age = age
    def p(self=True):
        print('это функция С')


class V(B, C):
    def __init__(self,name,age):
        # super().__init__(name)
        B.__init__(self,name)
        C.__init__(self,age)


# A.p()
# def p(self=True):
#     A.p()

p = V('Бегимай',10)  # A
p.p()
# A.p(p)
print(p.name,p.age)

print(V.mro())
