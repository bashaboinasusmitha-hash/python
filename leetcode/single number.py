#Single number
'''Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.'''
nums = [4,1,2,1,2]
n=len(nums)
dic={}
ans=0
for i in range(n):
    if nums[i] not in dic:
        dic[nums[i]]=1
    else:
        dic[nums[i]]+=1
#print(dic)
for j in dic:
    print(dic[j])
    if dic[j]==1:
        ans=j
print(ans)