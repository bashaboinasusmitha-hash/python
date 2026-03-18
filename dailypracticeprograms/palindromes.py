#about "isalnul():"
sentence="A man,a plan,a canal : Panama"
sentence=sentence.isalnum()
print(sentence)
#isalnum():checks whether the given input contains all the numbers or letters 
'''isalnum():returns true when:It returns True if the string has:
letters ✔
numbers ✔
or a mix of both ✔
As long as there are no spaces or special characters'''
#example:
print("abc123".isalnum())   # True
print("a1b2c3".isalnum())   # True
print("123".isalnum())      # True
print("abc".isalnum())      # True
#false condition:
print("abc 123".isalnum())  # False (space)
print("abc@123".isalnum())  # False (@ symbol)
print("123!".isalnum())     # False (! symbol)
#check a sentence is palindrome :
sentence=input("enter a sentence:").lower()
rev=""
sentence=sentence.lower()
print(sentence)
for char in sentence:
    #print(char)
    if char.isalnum():# here it checking that all characters are numbers or letters if it letters or numbers it adding to rev 
        rev=rev+char
palindrome=rev[::-1]
print(palindrome)
if palindrome==rev:
   print("Palindrome")
else:
   print("Not a palindrome!")
#checking a word palindrome:
word="moM".lower()
#rev=""
#rev=rev+char
palindrome=word[::-1]
if palindrome==word:
    print("Palindrome")
else:
    print("Not a palindrome!")