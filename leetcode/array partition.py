#Array partition:
'''Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
 such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum. '''
nums=[6,2,6,5,1,2]
nums.sort()
print(nums)
n=len(nums)
ans=0
for i in range(0,n,2):
    #print(nums[i])
    ans+=nums[i]
print(ans)