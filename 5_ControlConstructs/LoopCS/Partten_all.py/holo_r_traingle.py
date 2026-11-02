r = 7
'''for i in range(1,r+1):
    for j in range(1,i+1):
        if j == 1 or j ==i or i == r:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

for i in range(r):
    for j in range(r-i):
        if j == 0 or j == r - i -1 or i == 0: 
            print("*",end=" ")
        else:
            print("_",end=" ")
    print()