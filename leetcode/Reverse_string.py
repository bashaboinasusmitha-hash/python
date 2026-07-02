#reversing a string without using the another variable
s=["h","e","l","l","o"]
s.reverse()
print(s)
#method 2
s_1=[]
for i in range(len(s)-1,-1,-1):
    s_1.append(s[i])
print(s_1)
#method 3
for i in range(len(s)//2):
    s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
print(s)
#method 4
s=s[::-1]
print(s)