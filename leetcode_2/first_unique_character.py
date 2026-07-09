s="loveleetcode"
n=len(s)
dic={}
for i in s:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
first=None
print(dic)
for i in range(n):
    if dic[s[i]]==1:
        print(i)
        break
else:
    print(-1)
