num = int(input("Enter Your Number: "))
i = 0
sum = 0
while i < num:
    sum += (num%10)
    num = num//10
print(sum)