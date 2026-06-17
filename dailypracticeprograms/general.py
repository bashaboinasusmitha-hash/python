arr=[1,3,2,4,6]
print(arr*2)#[1,3,2,4,6,1,3,2,4,6]
print(2*3**3)#54 here first 3**3=27 then 2*27=54
s="pop"
n=len(s)
s_1=''
'''s_1=""
for i in s[::-1]:
    s_1+=i
if s==s_1:
    print("palindrome")
else:
    print("not an palindrome")
s_1=s[::-1]
if s_1==s[::-1]:
    print("palindrome")'''
for i in range(n-1,-1,-1):
    s_1+=s[i]
if s_1==s:
    print("palindrome")
else:
    print("not palindrome")
#finding a number is palindrome or not:
num=343
num_1=num
rev=0
while num>0:
    digits=num%10
    rev=rev*10+digits
    num=num//10
print(rev)
if rev==num_1:
    print("yes")
else:
    print("no")
#prime checker:
number=7
if number<=1:
    print("Not prime")
else:
    for i in range(2,number-1):
        if number%i==0:
            print("Not Prime")
            break
    else:
        print("prime")
#Find all prime numbers between 1 and N.
n=20
for i in range(2,n+1):
    count=0
    for num in range(2,i):
        if i%num==0:
            count+=1
    if count==0:
        print(i,end=" ")
print()
#Remove duplicate characters from a string while maintaining order
s="programming"
n=len(s)
s_1=""
for i in s:
    if i not in s_1:
        s_1+=i
print(s_1)
