nums=[3,2,2,3]
val=3
k=0
n=len(nums)
for i in range(0,n):
    if nums[i]!=val:
        nums[k]=nums[i]
        k=k+1
print(nums[:k])
print(k)