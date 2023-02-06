class A1:
    p=True
    def a(self):
        print('A')


class A2(A1):
    def A1(self):
        super().a()
    def a(self):
        print('A2')


class A3(A2):...

# print(dir(A2))
print(A1.mro())
print(A2.mro())