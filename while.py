#Q1--WAC to print numbers from 1 to 10:
'''i = 1
while i<11:
    print(i,end=" ")
    i+= 1'''
#O.P---1 2 3 4 5 6 7 8 9 10 


#Q2---WAC to print numbers from 1-5 but if number is equal to 3 don't print it:
'''i = 1
while i<6:
    if i == 3:
        i+=1
        continue
    else:
        print(i,end=" ")
        i += 1  '''
#O.P--1 2 4 5


#Q3---WAC to print numbers from 1-10 if number is equal to 5 then break the loop:
'''i = 1
while i < 11:
    if i == 5:
        break
    else:
        print(i,end=" ")
        i+=1'''
#O.P--1 2 3 4
        

#Q4--2 4 6 8 10 12 14 16 18 20  print in a line:
#Way-1
'''for i in range(1,21):
    if i % 2 == 0:
        print(i,end=" ")
        i+=1'''
#Way-2
'''i = 2
while(i < 21):
    print(i , end=" ")
    i += 2'''
#Way-3
'''i = 1
while i < 21:
    if i %2 == 0:
        print(i, end=" ")
    i+=1'''
#O.P--2 4 6 8 10 12 14 16 18 20 

#Q5--Creat Table
'''num = int(input("Enter Your Number: "))
for i in range(1,11):
    print(i*num,end=" ")'''
#O.P--Enter Your Number: 3
#3 6 9 12 15 18 21 24 27 30 

#Q6--Print number from 1-100:
'''i = 1
while i <= 100:
    print(i,end=" ")
    i+=1'''
  # O.P--1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100

#Q7--Print numbers from 100 to 1:
'''i = 100
while i >= 1:
    print(i,end=" ")
    i -= 1'''
#O.p--100 99 98 97 96 95 94 93 92 91 90 89 88 87 86 85 84 83 82 81 80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1


#Q8--Print the multiplecation table of a number n:
'''n = int(input('Enter Number: '))
i = 1
while i <= 10:
    print(i*n,end=" ")
    i+=1'''
#O.P-Enter Number: 2
#2 4 6 8 10 12 14 16 18 20 

#Q8--Print the list-[1,4,9,16,25,36,49,64,81,100]
'''list = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(list):
    print(list[idx],end=" ")
    idx+=1'''
#O.P--1 4 9 16 25 36 49 64 81 100 

#Q9--Search for a number x in this tuple using loop:
'''tuple = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter your search number: "))
i = 0
while i < len(tuple):
    if x == tuple[i]:
     print("idx:",i)
    i+=1'''
#O.P--Enter your search number: 25
#idx: 4


   #__Q(10)
#Reverse Number
n = int(input("Enter Your Number: "))
rev = 0
while(n>0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n//10
print(rev)
#O.P
#Enter Your Number: 123
# 321

#__Random Number___
import random
secret_number = random.randint(1,20)
attempts = 0

print("'1' se '20' tak koi bhi number guess karo jaldi....")
print(secret_number)
while True:
    guess = int(input())
    attempts+= 1
    if 1 >guess > 20:
        print("Invalid Number")

    elif guess < secret_number:
        print("Aur thoda Bada Number Sochiye")
    
    elif guess > secret_number:
        print("Aur thoda chota number sochiye")
    
    else:
        print(f"Mubarak ho aap '{attempts}' attempts mai sahi number guess kar paye...")
        break


#_____Fibonacci Series______
n = int(input())
a = 0
b = 1
count = 0
if n <= 0 :
    print("Give a Possitive Number")
elif n == 1:
    print(f"Fibonacci Series of 1: 0")
else:
    print("Fibonacci Series:")
    i =1
    while i < n:
        print(a,end=" ")
        c = a+b
        a = b
        b = c
        i+=1
print()
print(count)

#_____Stop When Negetive Number comes break the loop_____
while True:
    n = int(input())
    
    if n < 0:
        print("Negative Number")
        break

#______Sum Of Input Number_________
n = 1234
s = 0
i = 1
while i < n:
    s = s + (n%10)
    n = n/10

print(int(s))

#________Reverse Number___
n = 1234
riv = 0
i = 1
while 0 < n:
    riv = riv *10 + (n%10)
    n = n//10

print(riv)