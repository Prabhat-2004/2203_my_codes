day_of_weeks = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Saturday', 'Sunday')
print(day_of_weeks)
print(day_of_weeks[0])
print(day_of_weeks[3])
print(day_of_weeks[-1])
print(day_of_weeks.find("Monday"))



#Finding index of  numbe using tuple
tup = tuple(int(i) for i in input().split())
print(tup)
x = int(input())
if x in tup:
    ind = tup.index(x)
    print("At index:",ind)
else:
    print("Given number is not in tuple")