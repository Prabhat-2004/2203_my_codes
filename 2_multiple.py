class Father:
    def show_father(self):
        print("This is father class...")
class Mother:
    def show_mother(self):
        print("This is mother class...")
class Child(Father,Mother):
    def show_child(self):
        print("This is child class...")
c = Child()
c.show_child()
c.show_mother()
c.show_father()