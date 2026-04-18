num1="2"
num2="3"
num1=int(num1)
num2=int(num2)
print(num1*num2)
def multiply(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"
    n, m = len(num1), len(num2)
    res = [0] * (n + m)
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))   
            res[i + j + 1] += mul   
            res[i + j] += res[i + j + 1] // 10
            res[i + j + 1] %= 10
    return ''.join(map(str, res)).lstrip('0')
num1="2"
num2="3"
result=multiply(num1,num2)
print(result)
#lstrip() means left strip which removes the zeros oon left side of a number: 005896 actual ans is 5896 lstrip(0) removes zeros before actaull number.