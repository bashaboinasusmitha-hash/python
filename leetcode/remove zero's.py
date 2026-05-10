num = 102030
res = 0
while num > 0:
    digit = num % 10
    if digit != 0:
        res = res * 10 + digit
    num //= 10
# reverse the result
final = 0
while res > 0:
    final = final * 10 + (res % 10)
    res //= 10
print(final)