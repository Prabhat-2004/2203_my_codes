
class Add:
    def calculate(self,a,b):
        print(a+b)
class Mul:
    def calculate(self,a,b):
        print(a*b)
class Div:
    def calculate(self,a,b):
        print(a/b)
#Function using Duck type
def cal(ref):
    ref.calculate(10,20)

#Passing different objects to the same function
cal(Add()) #30
cal(Mul()) #200
cal(Div()) #0.5