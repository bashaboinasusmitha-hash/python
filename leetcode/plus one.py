digits = [1,2,3,5,5]
n = len(digits)
sum = digits[n-1]
for i in range(n-1, -1, -1):
    if digits[i] == 9:
        digits[i] = 0
        sum = 10
    else:
        digits[i] = digits[i] + 1
        sum = digits[i]
        break
if sum == 10 and digits[0] == 0:
    digits = [1] + digits
print(digits)