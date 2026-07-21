nums=[0,0,1,1,1,2,2,3,3,4]
n=len(nums)
i=0
k=0
while i<len(nums)-1:
    if nums[i]==nums[i+1]:
        nums.pop(i+1)
    else:
        i+=1
print(len(nums))
nums=[1,1,2]
k=1
for i in range(1,len(nums)):
    if nums[i]!=nums[i-1]:
        nums[k]=nums[i]
        k+=1
print(k)