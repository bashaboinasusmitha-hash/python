#Removing duplicates from sorted array:
nums=[0,0,1,2,3,3,4]
k=1
for i in range(len(nums)-1):
    if nums[i]!=nums[i+1]:
        nums[k]=nums[i+1]
        k=k+1
print(nums[:k])
print(k)