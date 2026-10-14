#Inheritance in a chain
class Grand_Father:
    def show_grand(self):
        print("This is Grand Father class...")
class Father(Grand_Father):
    def show_father(self):
        print("This is father class...")
class Child(Father):
    def show_child(self):
        print("This is child class...")
c = Child()
c.show_child()
c.show_father()
c.show_grand()