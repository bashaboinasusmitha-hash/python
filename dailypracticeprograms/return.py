'''def func(s1,s2):
    if s1==s2:
        return True
    return False
ans=func("abc","abcd")
print(ans)
#checking whether the words are equal or not:
def func(s1,s2):
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            return False
    return True
ans=func("and","and")
print(ans)
print(ans)
#Passing of dic to parameters:
def fun(a):
    print(a)#{1:4}
dic={1:4}
fun(dic)
#checking two hashmaps are equal:
def func(dic1,dic2):
    if dic1==dic2:
        return True
    return False
dic1={1:2,3:6}
dic2={1:2,3:2} 
ans=func(dic1,dic2)
print(ans) 
def fun(dic1,dic2):
    for i in range(len(dic1)):
        if dic1[i]!=dic2[i]:
            return False
    return True
dic1={1:2,3:6}
dic2={1:2,3:6,2:4} 
ans=func(dic1,dic2)
print(ans) 
def fun(dic1,dic2):
    if len(dic1)!=len(dic2):
        return False
    for i in dic1:
        if i not in dic2 or dic1[i] not in dic2:
            return False
    return True
dic1={1:2,3:6}
dic2={1:2,3:2} 
ans=func(dic1,dic2)
print(ans)'''      
#Anagrams:
s1="abcd"
s2="cba"
dic1={}
dic2={}
for i in s1:
    if i in dic1:
        dic1[i]+=1
    else:
        dic1[i]=1
for j in s2:   
    if j not in dic2:
        dic2[j]=1
    else:
        dic2[j]+=1
print(dic1)
print(dic2)
if len(dic1)!=len(dic2):
    print("NOT Anagrams")
elif dic1!=dic2:
    print("not anagrams")
else:
    print("Anagrams")