#Find the First Non-Repeating Character
string="programming"
n=len(string)
dic={}
for i in string:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for i in dic:
    if dic[i]==1:
        print(i)
        break
#find all the non repeating characters in a string:
string="susmiitha"
dic={}
for i in string:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for i in dic:
    if dic[i]==1:
        print(i)
#Find the Second Largest Element in a List
li=[7,7,7,7,7,7,7,7,7,7]
largest=li[0]
second_largest=float('-inf')
for i in li:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i!=largest:
        second_largest=i
if second_largest==float('-inf'):
    print("no second largest element")
else:
    print("Second largest element is:", second_largest)