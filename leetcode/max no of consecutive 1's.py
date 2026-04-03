#Find maximum consecutive ones by flipping atmost k 0's
'''Given a binary array nums and an integer k, return the 
maximum number of consecutive 1's in the array if you can flip at most k 0's.'''
nums=[1,1,1,0,0,0,1,1,1,1,0]
k=2
l=0
n=len(nums)
ans=0
temp=0
for r in range(n):
    if nums[r]==0:
        temp+=1
    while temp>k:
        if nums[l]==0:
            temp-=1
        l+=1
    ans=max(ans,r-l+1)
print(ans)