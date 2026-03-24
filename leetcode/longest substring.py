s="ababcab"
n=len(s)
dic={}
for i in range(n):
    for j in range(i,n):
        if s[i:j+1] not in dic:
            dic[s[i:j+1]]=1
        else:
            dic[s[i:j+1]]+=1
print(dic)
li=[]
for i in dic:
    li.append(i)
print(li)
for i in li:
    temp={}
    for j in i:
        if j not in temp:
            temp[j]=1
        else:
            temp[j]+=1
print(i,temp)
#Longest substring without repeating characters:
'''Given a string s, find the length of the longest substring without duplicate characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.'''
s = "ababcab"
seen = set()
left = 0
max_len = 0
longest = ""
for right in range(len(s)):
    # remove until no duplicate
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
        # add current character
    seen.add(s[right])   
    # update result
    if right - left + 1 > max_len:
        max_len = right - left + 1
        longest = s[left:right+1]
print("Length:", max_len)
print("Substring:", longest)