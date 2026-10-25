num = int(input("Enter Your Number: "))
rev = 0
i = 0
while i < num:
    rev = rev * 10 + (num%10)
    num //= 10
print(rev)