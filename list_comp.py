#With out list compherision
'''li = [11,22,33,44,55,66,77,88,99]
sqr_list = []
for i in li:
    sqr_list.append(i**2)
print(sqr_list)

#With list compherision
lis = [11,22,33,44,55,66,77,88,99]
sqrr_list = [i ** 2 for i in lis]
print(sqrr_list)

'''
#WAP to calculate the avg. of given list
'''li = input()
x = li.split()
sum = 0
print(x)
new_li = []
for i in x:
    new_li.append(int(i))
print(new_li)
for i in new_li:
    sum = sum + i
print(sum)

avg = sum / len(new_li)
print(avg)'''

#Wap to filtering given numbers from the given list and create a new list.
given_num = [11,22,33,44,12,23,34,556,778,987,65,66,45,46]

even_list = [i for i in given_num if i%2 == 0]
print(even_list)

'''#WAP to Finding Index 
li = input()
fi_ind = int(input())
se_ind = int(input())
sp_li = li.split()
print(sp_li)
int_li = list(map(int,sp_li))
# for i in sp_li:
#     int_li.append(int(i))
print(int_li)
slicee = int_li[fi_ind:se_ind]
print(slicee)'''

'''
# WAP to add +5 to each element of li and create a new list of it.
li = [15,25,35,45]
add_new = [i+5 for i in li]
print(add_new)
'''
'''
#WAp to finding shortest names and create a new list of it:
name = ['Preeti','Pila','Geli','Prabhat']
short_name = [i for i in name if len(i) < 7]
print(short_name)'''
x = [10,20,11,13,41,42,35,30,40,75,45,44,22,50,60,70,80,90]
'''sqp = []
for i in  x:
    sqp.append(i**2)
print(sqp)
'''
sqp = [i**2 for i in x]
print(sqp)

nl = [i+5 for i in x]
print(nl)

evnli = [i for i in x if i%2 == 0]
print(evnli)