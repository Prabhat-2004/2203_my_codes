class Kodnest:
    def __init__(self):
        self.__student = "Prabhat"
    def disp(self):
        print(self.__student) #Accessing Private Variable Inside the class
k = Kodnest()
k.disp()
print(k._Kodnest__student) #Accessing Private Variable Outside the class
'''Out Side the class Private variable is accessed 
wit using NameMangling(_ClassName__VariableName).'''
