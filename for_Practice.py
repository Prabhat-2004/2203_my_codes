#__Q(1)
#Wapp to print number from 1-10 using for loop:-
'''for i in range(11):
    print(i)'''


#__Q(2)
#Wapp to print numbers from 5 to 15 using for loop:-
'''for i in range(5,16,1):
    print(i)'''


#__Q(3)
#Wapp to print all even numbers from 1 to 10 using for loop:-
#Way-1
'''for i in range(1,11):
    if i % 2 == 0:
        print(i)'''
#Way-2
'''for i in range(2,11,2):
    print(i)
'''


#__Q(4)
#Wapp to print all odd numbers from 1 to 10 using for loop:-
#Way-1
'''for i in range(1,11,2):
    print(i)'''
#Way-2
'''for i in range(1,11):
    if i % 2 != 0:
        print(i)'''

#__Q(5)
#Wac to Print the list-[1,4,9,16,25,36,49,64,81,100]
'''list=[1,4,9,16,25,36,49,64,81,100]
idx = 0
for i in range(len(list)):
    if i == idx:
        print(list[idx],end=" ")
        idx+=1'''
#O.P--1 4 9 16 25 36 49 64 81 100 



#__Q(6)
#Wac to Search for a number x in this tuple using loop:
'''tuple = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter your number: "))
for i in range(len(tuple)):
    if x == tuple[i]:
        print("idx of the number is:",i,"  And the Number is:",tuple[i])
        i+=1'''
#O.P--Enter your number: 25
#idx of the number is: 4   And the Number is: 25

#__Q(7)
#Fibonacci series
'''num = int(input("Counting the numbr of fibonacci series: "))
a = 0
b = 1
for i in range(num):
    res = a+b
    print(a,end=' ')
    a,b=b,res'''
#O.P
#Counting the numbr of fibonacci series: 5
# 0 1 1 2 3 


#__Q(8)
#Sum of the number
'''n = int(input("Give your number: "))
sum = 0
for i in range(n):
    digit = n % 10
    sum = sum + digit
    n = n // 10
print(sum)'''
#O.P
#Give your number: 12345
# 15

    


