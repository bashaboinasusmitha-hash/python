#Finding max average of subarray which length is equal to k: 
nums=[-1]
k=1
n=len(nums)
l=0
ans=float("-inf")
temp=0
for r in range(n):
    temp+=nums[r]
    #print(temp)
    if r-l==k:
        temp-=nums[l]
        l+=1
    if r-l+1==k:
        print(nums[l:r+1])
        res=temp/k
        ans=max(res,ans)
print(ans)