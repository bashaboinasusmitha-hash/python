#finding largest word:
words=input("enter a words :").lower()
words=words.split(" ")
longest=""
#susmitha Tharun rama Ravinder
for i in words:
    if len(i)>len(longest):
        longest=i
print(longest)
#Check Palindrome Words in a Sentence
sentence=input("Enter the sentence:").lower()
words=sentence.split()
for i in words:
    n=len(i)
    if i[0]==i[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")