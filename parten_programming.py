#Q1___=
''''row = int(input("Enter the rows: "))
col = int(input("Entger the columns: "))
for i in range(row):
    print("* "*col)'''
#O.P
'''Enter the rows: 3
Entger the columns: 4
* * * * 
* * * *
* * * *'''

#Q2___= Rightangle traingle
'''
for i in range(5+1):
    print("* "*i)
    
OR

for i in range(1,5+1):
   for j in range(i):
      print("*",end=" ")
   print()
#O.P
* 
* *
* * *
* * * *
* * * * *'''
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
for i in range(row):
    for j in range(i,row-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("R",end=" ")
    print()
for i in range(row-1):
    for l in range(i+1):
        print(" ",end=" ")
    for j in range(i,row-1):
        print("R",end=" ")
    print()
print()
for i in range(row):
    for j in range(i+1):
        print("I" , end = " ")
    for k in range(2*(row-i-1)):
        print(" ",end=" ")
    for l in range(i+1):
        print("I",end=" ")
    print()
for i in range(4):
    for j in range(i,4):
        print("i" , end = " ")
    for k in range(2*(i+1)):
        print(" ",end=" ")
    for l in range(i,4):
        print("i",end=" ")
    print()

print()   


for i in range(row):
    for j in range(i,row):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=' ')
    for k in range(i+1):
        print("*",end=" ")
    print()
print()
for i in range(row):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(i,row-1):
        print("*",end=' ')
    for k in range(i,row):
        print("*",end=" ")
    print()
print()

for i in range(row):
    for j in range(i,row):
        print(" ",end=" ")
    for k in range(i):
        print("!",end=' ')
    for k in range(i+1):
        print("!",end=" ")
    print()

for i in range(4):
    for j in range(i+2):
        print(" ",end=" ")
    for k in range(i,4-1):
        print("i",end=' ')
    for k in range(i,4):
        print("i",end=" ")
    print()
print()



