#Finding Name And Score Using Nested Loop
n = int(input())
li = []
score_li = []
for i in range(n):
    name = input()
    score = float(input())
    score_li.append(score)
    li.append([name,score])
#print(li)
#print(score_li)
score_li = list(set(score_li))
sorted_list = sorted(score_li)
#print(sorted_list)
second_lowest = sorted_list[1]
#print(second_lowest)
names = []
for name, score in li:
    if score == second_lowest:
        names.append(name)
#print(names)
for i in  names:
    print(i)
