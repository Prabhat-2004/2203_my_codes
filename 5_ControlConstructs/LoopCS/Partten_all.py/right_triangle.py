#2. Right Triangle Pattern
r = 5
for i in range(r+1):
    print("* "*i)

#or

for i in range(r+1):
    for j in range(i):
        print("*",end=" ")
    print()

    