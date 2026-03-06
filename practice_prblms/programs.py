#finding common elements in two lists:
li1=[1,4,2,4,6,8]
li2=[1,7,3,8,9,3,2]
common=[]
for i in li1:
    if i in li2:
        common.append(i)
print(common)
#count digits space in sentence:
sentence=input("enter any sentence:")
digits=0
letters=0
space=0
for i in sentence:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        letters+=1
    elif i==" ":
        space+=1
print(digits)
print(letters)
print(space)
#Check Perfect Number:
#A number whose factors sum equals the number
num=int(input("enter a number"))
count=0
for i in range(1,num):
    if num%i==0:
        count+=i
if num==count:
    print(f"the number {num} is perfect number")
else:
    print("number is not a perfect number ")