row = 5
for i in range(row):
    for j in range(i+1):
        print("P",end=" ")
    print()
for i in range(row-1):
    for j in range(i,row-1):
        print("P",end=" ")
    print()
print()