class Employee:
    def __init__(self,name,id):
        self.emp_name = name
        self.emp_id = id
#Creating Object
e1 = Employee("PM",101)
e2 = Employee("Pk",102)

#Accessing Object
print("e1 Employee Name:", e1.emp_name)
print("e2 Employee Name:", e2.emp_name)
print("e1 Employee Id:", e1.emp_id)
print("e2 Employee Id:", e2.emp_id)