nums=[1,2,5,2,3]
target=3
nums.sort()
li=[]
for i in range(len(nums)):
    if nums[i]==target:
        li.append(i)

print(li)