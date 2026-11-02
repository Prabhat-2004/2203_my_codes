#Pyramid Star Pattern
r = 6
for i in range(r):
    print(" "*(r-i) + "* "*i)


#Or

for i in range(r):
    for j in range(r-i):
        print(" ",end="")
    for k in range(i):
        print("* ", end = "")
    print()

print()
print()

#inverted Pyramid
for j in range(r):
    print(" "*j + "* "*(r-j))
print()
 
#or

for j in range(r):
    for k in range(j):
        print(" ", end ="")
    for l in range(r-j):
        print("* ",end="")
    print()