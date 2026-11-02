r = 6
for i in range(r):
    for j in range(2 * r-1):
        if j == r+i-1 or j == r-i-1 or i == r-1:
            print("*",end="")
        else:
            print("_",end="")
    print()
    