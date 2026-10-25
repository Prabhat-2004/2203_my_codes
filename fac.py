#Factorial
num = int(input("Enter Your Number: "))
fac = 1
for i in range(1,num+1):
    fac *= i
print(fac)