#Search insert postion:
'''Given a sorted array of distinct integers and a target value, return the index if the target is found.
 If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.'''
nums=[1,3,5,6]
target=2
n=len(nums)
for i in  range(n):
    if nums[i]==target:
        print(i)
if target not in nums:
    nums.append(target)
    nums.sort()
#print(nums)
for i in range(len(nums)):
    if target==nums[i]:
        print(i)
#Using binary search:
nums=[1,3,5,6]
target=2
n=len(nums)
left=0
right=n-1
while left <= right:
    mid=(left+right)//2
    if nums[mid]==target:
        print(mid)
    elif nums[mid]<target:
        left =mid+1
    else:
        right=mid-1
else:
    print(left)