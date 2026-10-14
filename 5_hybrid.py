# Hybrid means combination of two or more inheritances...
class A:
    def show_a(self):
        print("This is A")
class B(A):
    def show_b(self):
        print("This is B")
class C(A):
    def show_c(self):
        print("This is C")
class D(B,C):
    def show_d(self):
        print("This is D")

#Creating object reference...
d = D()

#Accessing objects by using object reference..
d.show_d()
d.show_c()
d.show_b()
d.show_a()