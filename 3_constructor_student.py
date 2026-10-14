class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def learn(self):
        print(f"{self.name} is Very first learner...")
    def play(self):
        print(f"Roll No.-{self.id} is playing....")

#Object Creating
s1 = Student("AK",101)
s2 = Student("PK",102)
s3 = Student("RK",103)

#Accesing Veriables
print(s1.name)
print(s1.id)
s1.learn()
s1.play()
print()
print(s2.name)
print(s2.id)
s2.learn()
s2.play()
print()
print(s3.name)
print(s3.id)
s3.learn()
s3.play()