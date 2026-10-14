'''#Find last Digit of a number
number = float(input())
last_digit = number % 10
print(last_digit)'''

'''#WAPP to print a single charecter is vowel or not
ch = input()
if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("not vowel")'''

'''#WAPP to check number is even or odd
num = int(input())
if num % 2 == 0 :
    print("Even")
else:
    print("Odd")'''

'''#WAPP to check the 3rd last charecter is vowel or not
text = input()

if len(text) < 3 :
    print("Charecter is less than 3")
else:
    ch = text[-3]
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Not vowel")'''

'''#Check if the first and last number of a list is same or not. Take a pre-defined list in the code itself.
num = [10, 20, 30, 40,50, 10]
if num[0] == num[-1]:
    print("Same")
else:
    print("Not same")'''

'''#Calculate income tax for the input income by adhering to the Indian rules.
salary = float(input())
tax = 0
if salary <= 100000:
    tax = 0
elif salary <= 200000:
    tax = salary * 0.1
elif salary <= 300000:
    tax = salary * 0.2
else:
    tax = salary * 0.5
print(tax)'''

'''#Write a Python program to check whether a string starts with vowel or not.

ch = input()

if ch[0].lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")'''

'''WAP to calculate percentage of a student through 5 subjects. Take marks as input from the user.
Using percentage print which grade the student has scored'''

'''sub1 = float(input())
sub2 = float(input())
sub3 = float(input())
sub4 = float(input())
sub5 = float(input())

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total/500) *100

print("Mark:", total)
print("Percentage:", percentage, "%")'''

'''# WAP to convert a celsius value to fahrenheit. Take celsius value as input
celsius = float(input())
fahrenheit = (celsius * 9/5) +32
print(fahrenheit)'''

'''# WAP to print the day based on the number input.
day = int(input())
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("day")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Not valid a number")
'''

'''#WAP to check whether a person is eligible to vote or not based on their age.
age = int(input())
if age < 18:
    print("Age is not eligible to putting a vote")
else:
    print("Eligible for vote.")'''

'''#WAP to calculate the count of elements in a string.
string = input()
count = len(string)
print(count)'''

'''#WAP to check using the sides of a triangle to tell if it is equilateral triangle or not.

a = int(input())
b = int(input())
c = int(input())
if a == b == c :
    print("Its a equilateral Traingle")
else:
    print("Its not a equilateral Traingle.")

 '''

#WAP to check if the 2nd last digit of numerical input from the user is divisible by 3 or not.
num = input()
sec_last_dig = int(num[-2])
if sec_last_dig % 3 == 0:
    print("Its devisble by 3")
else:
    print("It is not devisible by 3")
    