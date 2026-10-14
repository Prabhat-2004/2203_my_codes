for i in "KODNEST":
    print(i,end=" ")

#__FACTORIAL__
n = int(input())
factorial = 1
if n < 0:
    print("Not a valid Number")
elif n == 0:
    print("Factorial of '0' is '1'")
else:
    for i in range(1, n+1):
        factorial*= i
print(factorial)

#__Reverse String___
x = input()
reverse = " "
for i in x:
    reverse = i + reverse
print(reverse)


#__Sum Of All Numbers___
u = int(input())
sum = 0
for i in range(1,u+1):
    sum+=i
print(sum)

#____Fibonacci Series_____
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
    for i in range(1,n+1):
        print(a,end=" ")
        c = a + b
        a = b
        b = c
        count+=1
print()
print(count)

#____Use Continue____
for i in range (1,51):
    if i % 5 == 0:
      continue
    else:
       print(i,end=" ")

#Panikiya
n = 2
for i in range(1,11):
    print(i*n)
    i+=1


