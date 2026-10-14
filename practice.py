def det(name,age,city,dist):
    print(f"Hello {name}, Welcome to in our World...!!!")
    print(f"Your age is {age}....!!!")
    print(f"And your city is {city} from {dist} District...!!!",end="\n\n")
det("Preeti","19","Bilahigarh","Rourkela")
det("Prabhat","20","Chatrapur","Ganjam")

#WAPP to addition of two numbers by taking inupt from user...!!!
'''WITHOUT PARAMETER WITHOUT RETURN VALUE'''
def addx():
   a = int(input("Enter 1: "))
   b = int(input("Enter 2: "))
   print("OUTPUT:",a+b)
addx()

'''WITH PARAMETER WITH RETURN VALUE'''
def add(a,b):
    return(a+b)
num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
res = add(num1,num2)
print("OUTPUT:",res)