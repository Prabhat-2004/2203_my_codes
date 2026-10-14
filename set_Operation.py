set1 = {1,2,3,4,5,6}
set2 = {1,2,3,4,5,6,7,8,9,0}

set3 = set1.union(set2)
print(set3)

set4 = set1.intersection(set2)
print(set4)


set5 = set2.update(set1)
print(set1)

set6 = set1.issubset(set2)
print(set6)

set7 = set1.issuperset(set2)
print(set7)

set8 = set2.issubset(set1)
print(set8)

set9 = set2.issuperset(set1)
print(set9)

set10 = set2.isdisjoint(set1)
print(set10)

set11 = set1.isdisjoint(set2)
print(set11)

#Symmetric_Difference
s1 = {10,20,30,40}
s2 = {20,25,30,35}
s_dif = sorted(list(s1.symmetric_difference(s2)))
print(s_dif)