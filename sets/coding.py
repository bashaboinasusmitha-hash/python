#remove duplicates:
li=[1,2,3,1,2,5,7,4,2]
a=set(li)
print(a)
#unique characters:
s=input("enter a string:")
a=list(s)#["s,"u","s","m","i","t","h","a"]
b=set(a)
print(b)
#counting the unique elements
li=[10,20,10,30,40,20]
count=0
n=len(li)
s=[]
for i in range(n):
    if li[i] not in s:
        s.append(li[i])
        count+=1
print(count)
#printing common elments
a=[1,2,3,4,5]
b=[4,5,6,7]
c=set(a)
d=set(b)
print(c.intersection(d))
#checking subset
a={1,2,3,4}
b={2,3}
print(a.issubset(b))
print(b.issubset(a))
#vowels in string:
vowels="aeiou"
word="programming"
a=set(word)
count=0
for i in a:
    if i in vowels:
        count+=1
print(count)
#finding a first repeating element
lst = [5,3,4,6,3,5,6]
s=[]
count=0
n=len(lst)
for i in lst:
    if i not in s:
        s.append(i)
    elif i in s:
        count=(i)
        break
print(count)
#more repeating elements:
li = [5,3,4,3,5,6,5]
s=set(li)
max_count=0
result=None
for i in s:
    ans=li.count(i)
    if ans>max_count:
        max_count=ans
        result=i
if max_count>1:
    print(f"most repeating element is {result}")
else:
    print("no repeating elements")