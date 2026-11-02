num = int(input("Enter Binary Number: "))
decimal = 0
power = 0
for i in range(num):
    digit = num % 10 
    decimal = decimal + digit * 2**power
    num = num//10
    power += 1
print(decimal)