#Intersection of arrays II:
'''Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.'''
nums1=[4,9,5]
nums2=[9,4,9,8,4]
dic={}
dic_1={}
for i in nums1:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for j in nums2:
    if j in dic_1:
        dic_1[j]+=1
    else:
        dic_1[j]=1    
print(dic)
print(dic_1)
li=[]
for i in dic:
    if i in dic_1:
        count=min(dic[i],dic_1[i])
        li.extend([i]*count)# here it is repeatinng the element i as count times.if i=3 and count=2 then using [i]*count=[3,3]
print(li)
nums1=[2,2,2]
nums2=[2,2]
res=[]
for num in nums1:
    if num in nums2:
        res.append(num)
        nums2.remove(num)
print(res)