li = [1,2,3,4,5]
def square(ele):
   return ele*ele
r=map(square,li)
print(r) # <map object at 0x000001E45FCBB8B0>
print(list(r)) # [1, 4, 9, 16, 25]


#Convert Str to int
li2 = ['10', '20', '30', '40', '50']
n_li2 = list(map(int,li2))
print(n_li2)  #[10, 20, 30, 40, 50]


#Convert int to float
li3 = [1,2,3,4,5,6,7]
n_li3 = list(map(float,li3))
print(n_li3) #[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]


#Convert int to bool
li4 = [1,2,3,4,0,6,0]
n_li4 = list(map(bool,li4))
print(n_li4) #[True, True, True, True, False, True, False]


#Countng numbers
li = [1,2,2,3,3,3,4,4,4,4]
for i in set(li):
    print(f"{i} occurs {li.count(i)} time(s)")



# Find average from the given list
numbers_list = list(map(int, input().split()))
sum = sum(numbers_list)
print(sum)
len =  len(numbers_list)
print(len)
avg = sum / len
print(avg)


#Extract the sub list
li = list(map(int,input().split()))
f_ind = int(input())
s_ind = int(input())
print(li[f_ind:s_ind])


# Print square from the given list
li = list(map(int,input().split()))
sqr = [i**2 for i in li]
print(sqr)

#Finding maximum and minimum
li = list(map(int,input().split()))
big = max(li)
sml = min(li)
print(big)
print(sml)

#Reverse the number
li = list(map(int,input().split()))
rev = li[::-1]
print(rev)

#Finding even and odd
li = list(map(int,input().split()))
ev = [i for i in li  if i % 2==0]
odd = [i for i in li  if i % 2!=0]
print(len(ev))
print(len(odd))


#Sum of all elements
tup = tuple(map(int,input().split()))
add = sum(tup)
print(add)

#Finding the index of an element in a tuple
tup = tuple(map(int,input().split()))
index_num = int(input())
if index_num in tup:
    ind = tup.index(index_num)
    print(ind)
else:
    print(f"{index_num} is not exist")

#Finding elements at even indeces
tup = tuple(map(int,input().split()))
ev = print(tup[::2])


#At one line
li = input()
print(li) #10 20 30 40 50
new_list = list(map(int,li.split()))
print(new_list) #[10, 20, 30, 40, 50]



#Find maximum and minimum
li = list(map(int,input().split())) #10 203 03 4040 4505 60
n = li[0]
for i in li:
    if n < i:
        n = i
print(n) #4040
for i in li:
    if n> i:
        n = i
print(n) #3




#Counting even number and odd number
li = tuple(map(int,input().split())) #11 22 33 44 55 66 77 88 99
eve = [i for i in li if i %2 == 0]
odd = [i for i in li if i %2 != 0]
print(len(eve)) #4
print(len(odd))#5