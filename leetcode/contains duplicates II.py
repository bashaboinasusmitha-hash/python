nums=[1,2,3,1,2,3]
k=2
n=len(nums)
found=False
for i in range(n-1):
    for j in range(i+1,n):
        if nums[i]==nums[j] and abs(i-j)<=k:
            found = True
        if found:
            break
else:
    print(found)
#sliding window approach:
nums = [1,0,1,1]
k = 1
window = set()
for i in range(len(nums)):
    if i > k:
        window.remove(nums[i - k - 1])   
    if nums[i] in window:
        print(True)
        break
    window.add(nums[i])
else:
    print(False)