#Finding all anagrams in a string:
def fun(dic1,dic2):
    if len(dic1)!=len(dic2):
        return False
    for i in dic1:
        if i not in dic2 or dic1[i]!=dic2[i]:
            return False
    return True
s="cbaebabacd"
p="abc"
n=len(s)
m=len(p)
l=0
ans=[]
dic1={}
dic2={}
for i in range(m):
    if p[i] not in dic2:
        dic2[p[i]]=1
    else:
        dic2[p[i]]+=1
for r in range(n):
    if s[r] not in dic1:
        dic1[s[r]]=1
    else:
        dic1[s[r]]+=1
    if r-l==m:
        lval=s[l]
        dic1[lval]-=1
        if dic1[lval]==0:
            dic1.pop(lval)
        l+=1
    if r-l+1==m:
        if fun(dic1,dic2):
            ans.append(l)
print(ans)