class Employee:
    company_name = "Unknown"
    employee_count = 0

    def __init__(self,name,age,emp_id):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        Employee.increment_employee()
    @staticmethod
    def company_policy():
        print("Company is a good company...")
    
    @classmethod
    def increment_employee(cls):
        cls.employee_count += 1

    def details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee Id: {self.emp_id}")
Employee.company_name  = "Mo Pila Company"
e1 = Employee("Prabhat", 21, 101)
e2 = Employee("Kumar", 22, 102)
e3 = Employee("Dakua", 23, 103)

print(Employee.company_name)
Employee.company_policy()
print('Employee Number:',Employee.employee_count)
e1.details()
e2.details()
e3.details()