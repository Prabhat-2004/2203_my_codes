class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def dog(self):
        print(f"{self.name} is a dog.")

class Cat(Animal):
    def cat(self):
        print(f"{self.name} is a cat.")

d = Dog("Toffy")
d.eat()
d.sleep()
d.dog()

c = Cat("Honey")
c.eat()
c.sleep()
c.cat()