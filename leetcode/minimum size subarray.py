#Minimum size subarray:
'''Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray 
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.'''
nums=[1,1,1,4,3]
target=7
n=len(nums)
l=0
ans=float("inf")
temp=0
for r in range(n):
    temp+=nums[r]
    while temp>=target:
        ans=min(ans,r-l+1)
        temp-=nums[l]
        l+=1
    #print(nums[l:r+1])
    print(nums[l:r+1])
if ans==float("inf"):
   print(0)
else:
    print(ans)