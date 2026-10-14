#Symmetric_difference
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
new_set = s1.symmetric_difference(s2)
print(new_set)
#Finding Difference
x = s1.difference(s2)
print(x) 

# #Finding Symmetric Difference between two sets and convert to list
# s3 = set(map(int,input().split()))
# s4 = set(map(int,input().split()))
# dif = sorted(s3.symmetric_difference(s4))
# print(dif)


#Sub_set
s5 = {1,2,3,4}
s6 = {1,2,3,4,5,6}
print(s5.issubset(s6)) 
#Common elements
print(list(s5.intersection(s6)))


#Dis_Joint
s7 = {1,2,3,4,5}
s8 = {6,7,8,9,0}
print(s7.isdisjoint(s8))

#Remove Duplicates: Given a list with duplicate elements, return a list with only unique elements.
li = [11,22,33,44,55,55,44,33,22,11,11,22,33,44,55,66,77,88,99,100,100,99,88,77,66,55]
print(list(set(li)))