class Demo:
    def __init__(self):
        self.name = "Preeti" #Public Access Modifier
    def dis(self):
        print(self.name) #Accessing public property inside own class - Allowed
d = Demo()
print(d.name) #Accessing public property ouside the class - Allowed
d.dis()

class Demo1(Demo):
    def disp(self):
        print(self.name)#Accessing public property inside child class - Allowed
d1 = Demo1()
d1.disp()

class Demo2:
    def display(self):
        print(d.name)#Accessing public property outside the class - Allowed
d2 = Demo2()
d2.display()