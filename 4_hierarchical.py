class Parent:
    def show_parent(self):
        print("Parent class")
class Baby_Girl(Parent):
    def show_girl(self):
        print("Baby_girl Class")
class Boy(Parent):
    def show_boy(self):
        print("Boy class")
    
#Creating Baby_girl object reference
g = Baby_Girl()
#Creating Baby_girl object reference
b = Boy()

#Accessing objects
g.show_girl()
g.show_parent()
b.show_boy()
b.show_parent()
