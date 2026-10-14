class Demo1:
    def __init__(self):
        self._name = "Preeti" #Protected Veriable
    def disp1(self):
        print(self._name) #Accessing inside the own class
d1 = Demo1()
d1.disp1()
class Demo2(Demo1):
    def disp(self):
        print(self._name) #Accessing inside the child class
d2 = Demo2()
d2.disp()
