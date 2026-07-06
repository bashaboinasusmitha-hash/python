'''print the students names of second lowest grades  from nested list,
if there are multiple same lowest grades then return the names by alphabetical order'''
li=[]
for i in range(int(input())):
    name = input()
    score = float(input())
    li.append([name,score])
print(li)
li_1=[]
for i in li:
    for j in i:
        if  isinstance(j,float):
            li_1.append(j)
scores=sorted(set(li_1))
second_score=scores[1]
names=[]
for i in li:
    if i[1]==second_score:
        names.append(i[0])
names.sort()
for i in names:
    print(i)