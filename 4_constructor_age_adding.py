class Student:
    def __init__(self,name,age,rollnumber):
        self.name = name
        self.age = age
        self.rollnumber = rollnumber

    def details(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll_No.: {self.rollnumber}")

    def update(self):
        self.age += 1
        print(f"Updated Age: {self.age}")

s1 = Student("prabhat",20, 101)
s1.details()
s1.update()