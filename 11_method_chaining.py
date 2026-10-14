class GreatGrandParent:
    def cook(self):
        print("Great Grand Parent fry patato....")
class GrandParent(GreatGrandParent):
    def cook(self):
        print("Grand Parent Cook Rice....")
class Parent(GrandParent):
    def cook(self):
        print("Praent Cook Pulao....")
        #super().cook()
class Child(Parent):
    def cook(self):
        print("Child cook Biriyani....")
        super().cook()
        #super(Parent,self).cook()
        #super(GrandParent,self).cook()
        GrandParent.cook(self)
        GreatGrandParent.cook(self)
c = Child()
c.cook()
