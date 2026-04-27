#Longest palindromic string:
'''Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.'''
s="ac"
n=len(s)
longest=''
for i in range(n):
    for j in range(i+1,n+1):
        sub=s[i:j]
        if sub==sub[::-1]:
            if len(sub)>len(longest):
                longest=sub
print(longest)