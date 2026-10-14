Student = {
    "name":"Preeti",
    "age":20,
    "Branch":"EEE",
    "Regd No.":2201305139,
    "sem":"7th",
    "n.name":"Preeti"
}
print(Student['n.name'])
print(type(Student),Student)
print(Student.keys())
print(Student.values())
Student["My_name"]="Prabhat"
print(Student)
del Student['n.name']
print(Student)
branch = Student.pop('Branch')
print(Student)
print(branch)
Student.items()
print(Student)
item = Student.items()
keys = Student.keys()
values = Student.values()
print(item)
print(keys)
print(values)

for i in Student:
    print(i,end=" ~ ")
print()
for i in Student.keys():
    print(i,end=" ~ ")
print()
for i in Student.values():
    print(i,end=" ~ ")
print()
for i in Student.items():
    print(i,end=" ~ ")