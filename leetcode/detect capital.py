'''word="USa"
n=len(word)
new_word=""
for i in range(n):
    if word[i].isupper():
        new_word+=(word[i])
print(len(new_word))
if len(word)==len(new_word):
    print("True")
else:
    print("False")'''
#detect capitals
'''We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.
 '''
word="FlaG"
n=len(word)
if word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower()):
    print("True")
else:
    print("False")