class MathOperation:
    @staticmethod
    def add(a,b): #<<<<<<< Class Lavel Method OR Static Method
      print(a+b)
    def sub(self,a,b):  #<<<<<< Instance Method
        print(a-b)
MathOperation.add(120,20) # <<< Class Lavel methods are directly oprtate with class name.
#MathOperation.sub(120,20) we can't access Inance methods with out creating any object reference.
m1 = MathOperation() # <<<<< Instance methoa are need to create a object reference variable.
m1.sub(111,11)
m1.add(10,20)
