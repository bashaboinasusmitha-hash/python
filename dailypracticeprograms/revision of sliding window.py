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