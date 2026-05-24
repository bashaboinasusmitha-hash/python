#dictionary programs:
'''Create a dictionary for a student:
Name
Roll number
Marks'''
dic={
    "Name":"Susmitha",
    "Age":23,
    "Marks":95
}
print(dic)
#Access dictionary values using keys.
for i in dic.keys():
    print(i)
a=dic.keys()
print(a)
b=dic.values()
print(b)
#adding new key value pair:
dic["Branch"]="CSE-AIML"
print(dic)
#Update dictionary values.
dic["Age"]=26
print(dic)
#Delete an item from dictionary.
del dic["Branch"]
print(dic)
#Find highest value in dictionary.
dic_1={"priya_m":95,"sushuuy_m":96,"tharun_m":93}
print(max(dic_1.values()))
maximum=float("-inf")
for i in dic_1.values():
    if i>maximum:
        maximum=i
print(maximum)
#Count frequency of characters in a string using dictionary.
s="susmithaasui"
dic={}
for i in s:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
#Conditional Statements
#Check whether a person is eligible to vote.:
age=int(input("enter u r age:"))
if age>=18:
    print("U r eligible for voting!")
else:
    print("Not eligible for voting!")
#Find greatest of three numbers.
li=[20,31,21]
maximum=li[0]
for i in li:
    if i>maximum:
        maximum=i
print(maximum)
letter=input("Enter a letter:").lower()
vowels="aeiou"
if letter in vowels:
    print("letter is vowel")
else:
    print("letter is consonant")
#Create a simple calculator using if-elif.
symbol=input("Enter a symbol:")
if symbol == "+":
    print("addition")
elif symbol== "-":
    print("subtraction")
elif symbol == "*":
    print("multiplication")
elif symbol=="%":
    print("modulo")
elif symbol=="/":
    print("division")
#Check whether a number is positive, negative, or zero.
number=int(input("Enter a number:"))
if number==0:
    
    print("number is zero")
elif number>0:
    print("number is positive")
elif number<0:
    print("number is negative")