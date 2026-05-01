# Find the Index of the First Occurrence in a String
'''Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
 or -1 if needle is not part of haystack'''
haystack="hello"
needle="ll"
n1=len(haystack)
k=len(needle)
ans=""
l=0
temp=[]
for r in range(n1):
    ans+=haystack[r]
    if r-l+1>k:
        ans=ans[1:]
        l+=1
    if r-l+1==k:
        temp.append(ans)
print(temp)
for i in range(len(temp)):
    if temp[i]==needle:
        print(i)
        break
else:
    print(-1)