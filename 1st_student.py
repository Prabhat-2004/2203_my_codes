class Student:
    name = "Mo Preeti"
    roll = 143
    def talk(self):
        print(f"I love to talk with {self.name}.")
    def study(self):
        print(f"{self.name} is like to study.")
    def eat(self):
        print(f"{self.name} is like to eat chocolate's, Icecream's and Panipuri.")
p = Student()
print(p.name)
print(p.roll)
p.talk()
p.study()
p.eat()