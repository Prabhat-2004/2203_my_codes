number = [0,1,2,3,4,5,6,7,8,9,10]

slice = number
print(slice)

slice_1 = number[2:6]
print(slice_1)

slice_2 = number[:5]
print(slice_2)

slice_3 = number[5:]
print(slice_3)

slice_4 = number[::2]
print(slice_4)

slice_5 = number[::3]
print(slice_5)

slice_6 = number[-3:]
print(slice_6)

slice_7 = number[1:10:2]
print(slice_7)


slice_8 = number[::]
print(slice_8)


slice_9 = number[0:5:3]
print(slice_9)

slice_10 = number[1::3]
print(slice_10)

n = [0,1,2,3,4,5,6,7,8,9]
print(n[6])
print(n[2:9])
print(n[3:])
print(n[:6])
print(n[::2])
print(n[::1])
print(n[::3])
print(n[-3:])
print(n[1:9:2])
print(n[::-1])

'''data = input()
li = data.split()
print(li)
new_li = [int(i) for i in li]
print(new_li)

avg = sum(new_li)/len(new_li)
print(avg)
'''
#Reverse a list: Write a function to reverse a list in-place and using slicing.
def reve(li):
    return li[::-1]
li = [10,20,30,40,50]
reverse_list = reve(li)
print(reverse_list)

#Flatten a nested list: Given [[1, 2], [3, 4], [5]], convert it to [1, 2, 3, 4, 5].
li = [[1,2],[3,4],[5]]
flatten = [item for sublist in li for item in sublist]
print(flatten)
'''or'''
new_li = []
for i in li:
    for x in i:
        new_li.append(x)
print(new_li)


#Slicing Given Number
li = input()
new_li = [int(i) for i in li.split()]
f_i = int(input())
l_i = int(input())
print(new_li)
x = new_li[f_i:l_i]
print(x)

#List Of squares using list comprehension
li = input()
new_li = [int(i) for i in li.split()]
sq_li = [i**2 for i in new_li]
print(sq_li)