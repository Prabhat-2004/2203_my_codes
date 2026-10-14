class Emp:
    college_name = "Nalanda" #Class Level Veriable
    def __init__(self,name,age):
        self.age = age #Instance Veriable
        self.name = name #Instance Veriable
e = Emp("Prabhat", 22)
print(e.age)
print(e.name)
#Class Level Veriable can be accessed by using class name or reference object.
print(e.college_name) #Instance Name
print(Emp.college_name)#Class Name

'''
________#CLASS LEVEL VERIABLES#__________________
-Class Level veriables are such veriables which are declered inside the class and out side any method.
-All objects for that class shares same copy of class veriable.

__________#Instance Veriable#______________________
-Instance veriables are such veribles which are present inside the object.
-for each object separate copy of instance veriables will be created.
'''