#Binary subarray with sum:
'''Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
A subarray is a contiguous part of the array.'''
def subarray(nums,k):
    if k<0:
        return 0
    n=len(nums)
    l=0
    ans=0
    temp=0
    for r in range(n):
        if nums[r]==1:
            temp+=1
        while temp>k:
            if nums[l]==1:
                temp-=1
            l+=1
        #print(nums[l:r+1])
        ans+=r-l+1
    return ans
nums=[0,0,0,0,0]
goal=0
a=subarray(nums,goal)
b=subarray(nums,goal-1)
ans=a-b
print(ans)