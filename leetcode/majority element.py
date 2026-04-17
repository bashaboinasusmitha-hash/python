#Majority element:
'''Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.'''
nums=[3,1,3]
n=len(nums)
dic={}
res=0
ans=n/2
for i in range(n):
    if nums[i] not in dic:
        dic[nums[i]]=1
    else:
        dic[nums[i]]+=1

for j in dic:
    if dic[j]>=ans:
        print(j)