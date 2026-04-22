#checking whether a number is prime or not:
num=int(input("Enter the number:"))
if num<=1:
    print("The number is not prime")
else:
    for i in range(2,num):
        if num%i==0:
            print("Number is not a prime.")
            break
    else:
        print("Number is a prime.")
#Finding factors of a number:
num=int(input("Enter a number:"))
for i in range(1,num+1):
    if num%i==0:
        print(i)