class Emp:
    college_name = "KK"
    def __init__(self, name):
        self.name = name
e1 = Emp("Preeti")
e2 = Emp("Mo_Pila")
# Class Level veriables can be accessed using object reference or class Name
print(e1.college_name)
print(e2.college_name)
print(Emp.college_name)

# CLASS LAVEL vs INSTANCE
'''
__CLASS LAVEL
> Class level variables are such variables which are declered  inside the class and outside any method.
> All objects for that class shares same copy of class variables.

__INSTANCE
> Instance variables are such variables which are present inside the object.
> For each object separate copy of instance variables are created.
'''