s="the sky is blue"
a=s.split()
b=a[::-1]
string=""
for i in range(len(b)):
    string+=b[i]
    if i!= len(b)-1:
        string+=" "
print(string)
#method 2:
b=a[::-1]
print(" ".join(b)) 