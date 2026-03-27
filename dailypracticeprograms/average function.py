#average function:
import math
def avg(*args):
    total=sum(args)
    count=len(args)
    return total/count
numbers=input("enter numbers:").split()
nums=[]
for i in numbers:
    nums.append(int(i))
print(f"{avg(*nums):.2f}")
#Reverse the words and swap the case of letters:
def reverse_words(sentence):
    words=sentence.split()
    words=words[::-1]
    s=""
    for word in words:
        for ch in word:
            if ch.islower():
                s+=ch.upper()
            else:
                s+=ch.lower()
        s+=" "
    return s.strip()    
a=input("enter a sentence:").strip()
print(reverse_words(a))    