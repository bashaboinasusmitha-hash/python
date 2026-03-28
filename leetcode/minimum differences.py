#finding minimum differences between highest and lowest k scores:
'''nums=[90]
n=len(nums)
k=1
temp=[]
ans=float("inf")
if len(nums)<=k:
    print(0)   
for i in range(n-1):
    for j in range(i+1,n):
        if nums[i]>nums[j]:
            diff=nums[i]-nums[j]
        else:
            diff=nums[j]-nums[i]
        ans=min(ans,diff)
print(ans)'''   
nums=[9,4,1,7]
nums.sort()
#print(nums)
n=len(nums)
k=2
ans=float("inf")
for i in range(n):
    for j in range(i,n):
        temp=[]
        for m in range(i,j+1):
            temp.append(nums[m])
        if len(temp)==k:
            last=temp[-1]
            first=temp[0]
            res=last-first
            ans=min(ans,res)
print(ans)
#sliding window approach
nums=[9,4,1,7]
nums.sort()
n=len(nums)
l=0
k=2
ans=float("inf")
temp=0
res=0
for r in range(n):
    if r-l==k:
        l+=1
    if r-l+1==k:
        ans=min(ans,nums[r]-nums[l])
print(ans)