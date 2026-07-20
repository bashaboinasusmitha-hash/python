#find the number of elements which are smaller than current element.
nums=[8,1,2,2,3]
ans=[]
for i in range(len(nums)):
    count=0
    for j in range(len(nums)):
        if nums[i]>nums[j]:
            count+=1
    ans.append(count)
print(ans)