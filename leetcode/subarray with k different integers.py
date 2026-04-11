#Subarray with k different integers.
def diffinteger(nums,k):
    n=len(nums)
    l=0
    ans=0
    temp=0
    dic={}
    for r in range(n):
        if nums[r] not in dic:
            dic[nums[r]]=1
        else:
            dic[nums[r]]+=1
        while len(dic)>k:
            dic[nums[l]]-=1
            if dic[nums[l]]==0:
                dic.pop(nums[l])
            l+=1
        ans=ans+r-l+1
    return ans
nums=[1,2,1,2,3]
k=2
a=diffinteger(nums,k)
b=diffinteger(nums,k-1)
print(a-b)