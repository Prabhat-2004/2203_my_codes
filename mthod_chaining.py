
class GreatGrandParent:
    def cook(self):
        print("Great Grand Parent Cooks AaluSija.")
class GrandParent(GreatGrandParent):
    def cook(self):
        print("Grand Parent Cooks Tarakari.")
class Parent(GrandParent):
    def cook(self):
        print("Parent Cookes Pakoda.")
        #super().cook()
class Child(Parent):
    def cook(self):
        print("Child Cookes Biriyani.")
        super().cook()
        super(Parent,self).cook()
        super(GrandParent,self).cook()

c = Child()
c.cook()
print(Child.mro())