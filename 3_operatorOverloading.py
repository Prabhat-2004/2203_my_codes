class Student:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
    def __add__(self,other):
        return self.name + other.name
    def __sub__(self,other):
        return self.name + other.name
    def __mul__(self,other):
        return self.name + other.name
    def __truediv__(self,other):
        return self.name + other.name
    def __floordiv__(self,other):
        return self.name + other.name
s1 = Student("Preeti")
print(s1) #Preeti

s2 = Student("Prabhat")
print(s2) #Prabhat

print(s1+s2) #PreetiPrabhat
print(s1-s2) #PreetiPrabhat
print(s1*s2) #PreetiPrabhat
print(s1/s2) #PreetiPrabhat
print(s1//s2) #PreetiPrabhat