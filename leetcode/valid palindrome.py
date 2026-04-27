#Valid Palindrome:
'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
 removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.'''
s="A man, a plan, a canal: Panama"
s=s.lower()
n=len(s)
res=""
for i in range(n):
    if s[i].isalnum():
        res+=s[i]
ans=""
m=len(res)
for i in (res[::-1]):
    ans+=i
if res==ans:
    print(True)
else:
    print(False)