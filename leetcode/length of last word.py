#Length of last word:
'''Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.'''
s= "   fly me   to   the moon  "
s=s.split()
n=len(s)
li=[]
for i in range(n):
    #if s[i] not in li:
    li.append(s[i])
print(li)
m=len(li)
print(m)
for i in range(m):
    if li[i]==li[m-1]:
        print(len(li[m-1]))
s="hello world"
s=s.split()
print(s)
for word in s:
    if word==s[-1]:
        print(len(word))