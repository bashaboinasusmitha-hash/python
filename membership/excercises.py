#problems:
li=[50,20,42,80,29]
num=int(input("Enter a number:"))
if num in li:
    print("number is found")
else:
    print("not found")
#vowel checker:
vowels="aeiou"
char=input("Enter a character:")
if char in vowels:
    print("it is a vowel")
else:
    print("it is a consonant")
#dictionary key and value checker
dic={"name":"ramu","age":30,"village":"nagaram"}
key=input("Enter a key:")
if key in dic:
    print("key found")
value=input("enter a value")
dic=dic.values()
if value in dic:
    print("value found")
#password character checker
password=input("enter a password:")
digits="0123456789"
characters="@!$%^&#"
has_digits=False
has_characters=False
for ch in password:
    if ch in digits:
        has_digits=True
    if ch in characters:
        has_characters=True
    if has_digits and has_characters:
        break
if has_digits and has_characters:
    print("valid password")
else:
    print("invalid password")
#printing common elements
a=[2,4,6,8]
b=[1,3,5,4]
for i in a:
    if i in b:
        print(i)
#substring counter
text="banana"
n=len(text)
count=0
for i in range(n):
    if text[i:i+2]=="an":
        count+=1
print(count)
#case insensitive check
text="i love python programming"
word=input("enter any word")
word=word.lower()
if word in text:
    print("word found")
else: 
    print("not found")
print([] in [1,2,3])
print(1 in [1,2,3])
print([1] in [1,3,2])