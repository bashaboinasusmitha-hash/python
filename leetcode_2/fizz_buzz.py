'''Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.'''
n=16
li=[]
for i in range(1,n+1):
    li.append(str(i))
    if i%3==0 and i%5==0:
        li.insert(i,"fizzbuzz")
        li.pop(i-1)
    elif i%3==0:
        li.insert(i,"fizz")
        li.pop(i-1)
    elif i%5==0:
        li.insert(i,"buzz")
        li.pop(i-1)
print(li)
n = 16
li = []
for i in range(1, n + 1):
    li.append(str(i))
    if i % 3 == 0 and i % 5 == 0:
        li[-1] = "fizzbuzz"
    elif i % 3 == 0:
        li[-1] = "fizz"
    elif i % 5 == 0:
        li[-1] = "buzz"
print(li)