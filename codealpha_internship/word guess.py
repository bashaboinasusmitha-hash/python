import random
li=["Apple","Plant","Cherry","Banana","Guava"]
li_1=[]
for i in li:
    i=i.lower()
    li_1.append(i)
#print(li_1)
n=len(li_1)
total_guess=6
attempts=0
x=random.choice(li_1)
word=x
word_len=len(word)
res=["_"]*len(word)
guessed_letter=[]
#print(word)
while total_guess>0 and "_" in res:
    letter=input("Enter a letter:")
    letter=letter.lower()
    if letter in guessed_letter:
        print("letter already guessed!")
        continue
    guessed_letter.append(letter)
    if letter in word:
        print("correct letter!")
        for i in range(len(word)):
            if word[i]==letter:
                res[i]=letter
        print(" ".join(res))
    else:
        attempts+=1
        total_guess-=1
        print(f"u have {total_guess} chances!")
if "_" not in res:
    print(f"u have won the game, the word is: {word}")
else:
    print(f"u have lost the game!,the word is:{word}")