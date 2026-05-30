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