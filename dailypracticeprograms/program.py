#finding highest sum of subarray of length : 3
nums=[5,9,1,8,7]
n=len(nums)
ans=0
for i in range(n):
    for j in range(i,n):
        temp=[]
        sum=0
        for k in range(i,j+1):
            temp.append(nums[k])
            sum+=nums[k]
        if len(temp)==3:
            ans=max(ans,sum)
print(ans)
#using sliding window approach:
nums=[5,9,1,8,7]
n=len(nums)
l=0
temp=0
k=3
ans=0
for r in range(n):
    temp+=nums[r]
    if r-l==3:
        temp-=nums[l]
        l+=1
    if r-l+1==3:
        ans=max(ans,temp)
print(ans)