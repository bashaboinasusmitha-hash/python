nums= [-1,10,6,-7]
n=len(nums)
li=[]
ans=-1
for i in nums:
    if i<0:
        li.append(i)
largest=li[0]
final=[]
for j in li:
    j=j*(-1)
    if j in nums:
        final.append(j)
if final:
    print(max(final))
else:
    print(ans)