#Find the second largest number in a list:
nums=[1,5,0,3,2,7]
largest=float("-inf")
second=float("-inf")
for i in nums:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print(second)
#print largest element without in built function:
nums=[3,10,4,7,3,2]
largest=nums[0]
for i in nums:
    if i>largest:
        largest=i
print(largest)
#finding smalllest element:
nums=[3,10,4,7,3,2]
smallest=nums[0]
for i in nums:
    if i<smallest:
        smallest=i
print(smallest)
#Remove duplicates from a list
nums=[10,3,2,2,5,7,3,10]
li=[]
for i in nums:
    if i not in li:
        li.append(i)
print(li)
#Count frequency of each character in a string
s="susmithaam"
dic={}
for i in s:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
#Find common elements in two lists
nums1=[10,4,2,7,3]
nums2=[4,8,9,3,7]
li=[]
for i in nums1:
    if i in nums2:
        li.append(i)
print(li)