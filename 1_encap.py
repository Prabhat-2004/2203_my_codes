class Person:
    def __init__(self,name,roll,age):
        self.name = name #public
        self._roll = roll #Protected
        self.__age = age #private
    def get(self):
        return self.__age
    def set(self,new_age):
        self.__age = new_age

p = Person("Preeti", 143, 20)
print("Name:",p.name)
print("Age: ",p._roll)
#print("Age: ",p.__age)  Error
print("Age: ",p.get())
p.set(21)
print("Updated Age:",p.get())