class Employee:
    company = "Code"
    def work(self):
        print(f"{self.name} is working...")
    def play(self):
        print(f"{self.name} is playing...")
e1 = Employee()
e2 = Employee()
e1.name = "Ak"
e1.id = 101
e2.name = "Pk"
e2.id = 102
e1.work()
e2.work()
e2.play()