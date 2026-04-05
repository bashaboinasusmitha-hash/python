#finding longst substring without repeating characters:
s="abcabbab"
res=set()
n=len(s)
l=0
ans=0
for r in range(n):
    if s[r] not in res:
        res.add(s[r])
    else:
        while s[r] in res:
            res.remove(s[l])
            l+=1
        res.add(s[r])
    ans=max(ans,r-l+1)
print(ans)