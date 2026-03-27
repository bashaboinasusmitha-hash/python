s="aababcabc"
n=len(s)
ans=0
for i in range(n):
    for j in range(i,n):
        temp=[]
        for k in range(i,j+1):
            temp.append(s[k])
        if len(temp)==3 and len(set(temp))==3:
            ans+=1
print(ans)
#sliding window approach:
s="aababcabc"
n=len(s)
temp=[]
ans=0
k=3
l=0
for r in range(n):
    temp.append(s[r])
    if r-l==k:
       temp.pop(0)
       l+=1
    if r-l+1==k and len(set(temp))==k:
        ans+=1
print(ans)
#using dictionaries:
s="abbabcabc"
n=len(s)
l=0
k=3
ans=0
dic={}
for r in range(n):
    if s[r] in dic:
        dic[s[r]]+=1
    else:
        dic[s[r]]=1
    if r-l==k:
        dic[s[l]]-=1
        if dic[s[l]]==0:
            dic.pop(s[l])
        l+=1
    if len(dic)==3:
        ans+=1
print(ans)