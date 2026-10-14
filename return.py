#1
def re():
    return 10
    return 20
    return 30
x = re()
print(x)

#2
def dis():
    return 10, 20, 30
    return 20
    return 30
d = dis()
print(d)
for i in d:
    print(i)