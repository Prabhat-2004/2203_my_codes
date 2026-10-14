class Student:
    clg_name = "Kalam Inistitu of technology"

    def __init__(self, name, age, clss):
        self.name = name
        self.age = age
        self.clss = clss
    @classmethod
    def change_clg_name(cls, new_name):
        cls.clg_name = new_name

    def attend_clss(self):
        print(f"{self.name} is attending the class({self.clg_name})")
    


s1 = Student("Prabhat", 20, "B-tech")
s2 = Student("Preeti", 20, "+3")

s1.attend_clss()
s2.attend_clss()
Student.change_clg_name("KK clg")
s1.attend_clss()
s2.attend_clss()
s1.change_clg_name("Sanskar Institute")
s1.attend_clss()
s2.attend_clss()



    
        