nums=[4,4,2,4,3]
n=len(nums)
ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if nums[i]!=nums[j] and nums[j]!=nums[k] and nums[i]!=nums[k]:
                print(i,j,k)
                ans+=1
print(ans)