class Employee:
    name = 'Priya'
    age = 33
    def teach(self):
        print('Employee is teaching...')
e1 = Employee()
e2 = Employee()
print(e1.name)
print(e2.name)
e1.teach()
e2.teach()
'''
1.The methods which are present inside the call are clled as Instance(object) Method. 
2.Self parameter is must when we declare a method inside a class.
'''