class MathOperation:
    @staticmethod
    def add(a,b):
        print(a+b)
    @staticmethod
    def sub(a,b):
        print(a-b)
    
    def mul(self,a,b):
        print(a*b)
    def div(self,a,b):
        print(a/b)
#Accessed using by @staticmethod (Class Name)
MathOperation.sub(20,10) # By using class name access the static method
MathOperation.add(10,20) # By using class name access the static method

#Creating Object Reference Veriable
m = MathOperation()
m.mul(10, 20) #Accesing instance method by using object reference veriable and we can't access using class name
m.div(10,20) #Accesing instance method by using object reference veriable and we can't access using class name
m.add(10,30) # Using object reference veriable we can access Static Method or class name..
m.sub(20,40) ## Using object reference veriable we can access Static Method or class name...
