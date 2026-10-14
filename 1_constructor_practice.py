class Employee:
    def __init__(self):
        self.name = "PM"
        self.id = "143"
#Creating Object
e1 = Employee()
e2 = Employee()

#Accessing instance veriables
print('Employee Name:',e1.name)
print('Employee Id:',e1.id)
print('Employee Name:',e2.name)
print('Employee Id:',e2.id)