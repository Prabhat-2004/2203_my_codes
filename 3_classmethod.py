class Student:
    clg_name = "Kalam"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod #Using clessmethod decorator
    def change_clg_name(cls,new_clg_name): #using classmethod
        cls.clg_name = new_clg_name
        print(cls.clg_name)
    def attendence(self): #instance method
        print(f"Name: {self.name}, Age : {self.age}")
#Creating Object Reference
s1 = Student("Preeti", 20)
s2 = Student("Prabhat", 21)

#Accessing
print("College Name:",Student.clg_name) # Accessing by using class name
Student.change_clg_name("Changed College Name: Kk") #Accessing by using classmethod
s1.attendence() #accessing by using instance object reference
s2.attendence() #accessing by using instance object reference
s1.change_clg_name("Mo Pila") #We can access class method by using object reference
s2.change_clg_name("Mo Wifeeee") ##We can access class method by using object reference