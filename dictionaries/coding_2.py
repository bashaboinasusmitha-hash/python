#frequency count:
li=[1,2,2,3,1,4,2]
n=len(li)
dic={}
for i in range(n):
    if li[i] not in dic:
        dic[li[i]]=1
    else:
        dic[li[i]]+=1
print(dic)
#first non repeating character:
s="programming"
li=list(s)
#print(li)
n=len(li)
dic={}
for i in range(n):
    if li[i] not in dic:
        dic[li[i]]=1
    else:
        dic[li[i]]+=1
print(dic)
for i in dic:
    if dic[i]<=1:
        print(i)
        break
#merge two dictionaries:
dic={"a":10,"b":20,"c":30}
dic_1={"name":"susmitha","age":20}
dic.update(dic_1)
print(dic)
#two sums problem:
nums = [2,7,11,15]
target = 9
dic = {}
for i in range(len(nums)):
    complement = target - nums[i]
    if complement in dic:
        print([dic[complement], i])
        break
    dic[nums[i]] = i
#group anagrans:
words=["eat","tea","tan","ate","nat","bat"]
dic={}
for i in words:
    key="".join(sorted(i))
    if key in dic:
        dic[key].append(i)
    else:
        dic[key]=[i]
print(list(dic.values()))