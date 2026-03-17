nums=[2,5,5,15]
target=10
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
             print([i,j])
#merge two sorted lists:
list1=[1,2,4]
list2=[1,3,4]
list3=(list1+list2)
print(list3)
for i in range(0,len(list3)):
    a=sorted(list3)
print(a)
#finding median of two arrays:
nums1=[1,2]
nums2=[3,4]
a=sorted(nums1+nums2)
n=len(a)
if n%2==0:
    median=(a[n//2-1]+a[n//2])/2
else:
    median=a[n/2]
print(round(median,4))