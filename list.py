list= ["Mango","Apple","Banana","Graaps","Chiku"]
print(list,type(list))
print(list[4])
print(list[0])
print(list[2])

# data = ["Apple",2,2+3j,22.3,True]
# print(data)
list.append("Orange")
print(list)

list.remove("Apple")
print(list)


del list[2]
print(list)

list.insert(0,"Pineaoole")
print(list)

print(list.pop())
list.pop()
print(list)

print(len(list))

for fruit in list:
    print(f"Your ordered fruit is {fruit}")

del list
print(list)

#Sort Method
s3 = [22, 12, 3, 21, 42, 33]
print(s3)
s3.sort()
print(s3)

print()

#Sorted Method
s4 = [33,22,10,34,21,31]
s4 = sorted(s4) #Any reference value needed
print(s4)

#Sqr of list
s = (list(map(int, input().split())))
print(s)
sqr = []
#sqr = [i*i for i in s]
for i in s:
    sqr.append(i**2)
print(sqr)

