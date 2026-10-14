class A:
    def show_A(self):
        print("This is A class.")
class B(A):
    def show_B(self):
        print("This is B class.")
class C(A):
    def show_C(self):
        print("This is C class.")
class D(B,C):
    def show_D(self):
        print("This is D class.")
d = D()
d.show_A()
d.show_B()
d.show_C()
d.show_D()