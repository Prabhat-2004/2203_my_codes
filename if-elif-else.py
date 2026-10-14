#__Q(1)___
Salary = int(input("Enter Your Salary"))
if Salary < 3500:
    tax = 0.2 * Salary
elif Salary < 10000:
    tax = 0.4 * Salary
elif Salary < 20000:
    tax = 0.6 * Salary
else:
    tax = 0.9 * Salary
print(f"Your Salary is {Salary} and Tax is {tax}")


#__Q(2)___
num = int(input("Enter Number"))
if num < 0:
    print(f"{num} is Negative")
elif num > 0:
    print(f"{num} is Possitive")
else:
    print(f"{num} is Zero")


#__Q3__
age = int(input())

if 0 < age <= 12:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
elif 20 <= age <= 64:
    print("Adult")
elif age <= 0:
    print("Invalid Age")
else:
    print("Senior")


#__Q4__
n = int(input())
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print("Invalid Number")

#___Q5___LEAF YEAR
year = int(input())
if year % 400 == 0:
    print("Its A Leaf year")
elif year % 100 == 0:
    print("Its not a leaf year")
elif year % 4 == 0:
    print("Its A Leaf Year")
else:
    print("Not A Leaf Year")

#__Mark Grade__
mark = int(input())

if mark >= 90:
    print("A")
elif 70 <= mark <= 89:
    print("B")
elif 50 <= mark <= 69:
    print("c")
else:
    print("Fail")

    