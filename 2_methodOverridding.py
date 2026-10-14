class Parent:
    def cook(self):
        print("Parent Cook Pulao...")
    def learn(self):
        print("Parent learning English...")
class Child(Parent):
    def play(self):
        print("Child playing Cricket...")
    def learn(self):
        print("Child learning Pyhton...")
c = Child()
c.cook() #Inherited Method
c.learn() #Overridden Method
c.play() #Spealized Method
