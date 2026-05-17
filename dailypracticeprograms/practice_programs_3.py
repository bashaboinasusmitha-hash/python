#Take a float number and convert it into integer.:
num=float(input("Enter a number:"))
ans=int(num)
print(ans)
#Convert integer to string and concatenate with another string.:
number=int(input("enter a number:"))
string="hey"
ans=str(number)
print(string+ans)
#Write a program to check whether a given value is Boolean or not.
boolen=True
print(type(boolen))
a=54
b=34
print(type(a==b))
#Convert string to uppercase and lowercase:
string="susMItHa"
a=string.lower()
b=string.upper()
print(a)
print(b)
#Reverse a string.
word="ramadevi"
print(word[::-1])
#Check whether a string is palindrome.
word="levela"
reverse=word[::-1]
if word==reverse:
    print("given word is palindrome.")
else:
    print("not a palindrome.")
#Count vowels in a string
word="susmithaa"
vowels="aeiou"
count=0
for i in word:
    if i in vowels:
        count+=1
print(count)
#Remove spaces from a string
sent="helo how r u"
ans=""
for i in sent:
    if i!=" ":
        ans+=i
print(ans)
#Count how many times a character appears in a string.
word="susmiithaa"
dic={}
for i in word:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
#Replace one word with another in a sentence:
sent="hey hello susmitha."
ans=sent.replace("hello","how r u")
print(ans)