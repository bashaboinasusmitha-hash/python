#Sort a list without using sort()
nums=[2,9,1,6,3]
n=len(nums)
for i in range(n-1):
    for j in range(0,n-i-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums)
#Find all substrings of a string
s="suma"
n=len(s)
ans=[]
for i in range(n):
    for j in range(i,n):
        temp=""
        for k in range(i,j+1):
            temp+=s[k]
        ans.append(temp)
print(ans)
#Move all zeros in a list to the end
nums=[1,5,2,0,3,0,2,1]
n=len(nums)
res=[]
zero=[]
for j in range(n):
        if nums[j]!=0:
            res.append(nums[j])
        else:
            zero.append(nums[j])
res.extend(zero)
print(res)
#Check if two strings are anagrams
#using sorted()
s1="abcs"
s2="scbb"
n1=len(s1)
n2=len(s2)
if n1==n2 and sorted(s1)==sorted(s2):
    print("Anagrams")
else:
    print("Not anagrams")
#by dictionary frequency count
s1="aksc"
s2="gtsc"
dic1={}
dic2={}
if len(s1)!=len(s2):
    print("not anagrams")
else:
    for i in s1:
        if i not in dic1:
            dic1[i]=1
        else:
            dic1[i]+=1
    for j in s2:
        if j not in dic2:
            dic2[j]=1
        else:
            dic2[j]+=1
print(dic1)
print(dic2)
if dic1==dic2:
    print("anagrams")
else:
    print("not anagrams")