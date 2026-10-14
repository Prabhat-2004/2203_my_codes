#Q1--Wac to print the number from 1 - 100 , if number is equal to 75 then break it:
'''i = 1
while i <= 100:
    print(i,end=" ")
    if i == 75:
        break
    i+=1'''
#O.P--1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75


#Q2--WAC to print the touple:
tuple = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter your search number: "))
i = 0
while i < len(tuple):
    if x == tuple[i]:
     print("idx:",i)
     break
    else:
       print("Invalid")
    i+=1
'''Enter your search number: 16
Invalid
Invalid
Invalid
idx: 3'''

#If negetive number comes loop is breaked
while True:
    n = int(input())
    
    if n < 0:
        print("Negative Number")
        break
search_list = ["apple", "banana", "cherry", "date"]

#____Searching In Lins_______
for fruit in search_list:
    if fruit == "cherry":
        print("Found it!")
        break  # Immediately jumps out of the loop
    print(f"Checking {fruit}...")
    