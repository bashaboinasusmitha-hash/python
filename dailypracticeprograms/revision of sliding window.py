nums=[1,1,2,1,1]
n=len(nums)
ans=[]
for i in range(n):
    for j in range(i,n):
        temp=[]
        for k in range(i,j+1):
            temp.append(nums[k])
        if len(temp)==3:
            ans.append(temp)
print(ans)
#sliding window approach printing the subarys whose length is k:
nums=[5,9,1,8]
n=len(nums)
k=3
l=0
temp=[]
ans=0
for r in range(n):
    temp.append(nums[r])
    if r-l==k:
        temp.pop(0)
        l+=1
    if r-l+1==k:
        print(temp)
#finding highest subarray sub whose lenght is k:
nums=[5,9,1,8]
n=len(nums)
l=0
temp=0
ans=0
k=3
for r in range(n):
    temp+=nums[r]
    if r-l==k:
        temp-=nums[l]
        l+=1
    if r-l+1==k:
        ans=max(ans,temp)
print(ans)#18