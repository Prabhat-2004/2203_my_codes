class Parent:
    def show_parent(self):
        print("This is Parent Class.")
class Child(Parent):
    def show_child(self):
        print("This is Child Class.")

c = Child()
c.show_parent()
c.show_child()