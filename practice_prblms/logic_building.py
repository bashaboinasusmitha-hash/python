#removing duplicates
li=[1,3,6,1,3,4,5]
n=len(li)
li_1=[]
for i in range(n):
    if li[i] not in li_1:
        li_1.append(li[i])
print(li_1)
#counting vowels in a sentence:
sentence=input("enter a sentence:")
vowels=["a","e","i","o","u"]
count=0
for i in vowels:
    for j in sentence:
        if i==j:
            count+=1
print(count)
#second largest number in a list:
li=[1,3,6,29,43,42]
largest=float("-inf")
second=float("-inf")
for i in range(len(li)):
    if li[i] > largest:
        largest=li[i]
        second=largest
    else:
        largest!=li[i] and second==li[i]
        second=li[i]
print(second)
#word frequency:
sentence=input("enter a sentence :")
sentence=sentence.split()
n=len(sentence)
sent=[]
for i in sentence:
    if i not in sent:
        sent.append(i)
        count=0
        for j in sentence:
            if i==j:
                count+=1
        print(f"the word {i} occurs {count} times")