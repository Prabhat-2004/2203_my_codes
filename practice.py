'''class Emplyee:
    name = 'Prahat'
    age = 21

    def teach(self):
        print("Teach students")
e1 = Emplyee()
e2 = Emplyee()

print(e1.name)
print(e2.age)
e1.teach()
e2.teach()'''


class Employee:
    company_name ="code"
    def work(self):
        print(f'Company: {self.company_name}, Name: {self.name}, UID: {self.id}, Employee is on work')
    def play(self):
        print(f"Company: {self.company_name}, Name: {self.name}, UID: {self.id},Employee in playGround")

e1 = Employee()
e1.name = "Ramesh"
e1.id = 373
e1.work()
print()
e2 = Employee()
e2.name = "Rajesh"
e2.id = 383
e2.work()
e2.play()
