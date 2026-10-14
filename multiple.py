class Father:
    def show_father(self):
        print("This is Father Class.")
class Mother:
    def show_mother(self):
        print("This is Mother Class.")
class Child(Father, Mother):
    def show_child(self):
        print("This is Child Class.")
c = Child()
c.show_father()
c.show_mother()
c.show_child()