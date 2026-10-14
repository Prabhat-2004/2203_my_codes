class Demo1:
    def __init__(self):
        self.__name = "Preeti" #Private Veriable
    def disp1(self):
        print(self.__name) #Accessing inside the own class
d1 = Demo1()
d1.disp1()
#print(d1.self.__name) Accessing outside the class is not allowed
class Demo2(Demo1):
    def disp(self):
        #print(self._name) #Accessing inside the child class is not allowed
        pass
d2 = Demo2()
d2.disp()
