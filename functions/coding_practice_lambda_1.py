#Write a lambda function to multiply three numbers.
mul=lambda x,y,z:x*y*z
print(mul(2,4,3))#24
#Write a lambda function to find the largest among two numbers.
largest=lambda x,y: x if x>y else y
print(largest(3,6))#6
#Write a lambda function to check whether a number is even or odd.
even_odd=lambda x: "even" if x%2==0 else "odd"
print(even_odd(4))#even
#Write a lambda function to check whether a number is positive or negative
pos_neg=lambda x: "positive" if x>=0 else "negative"
print(pos_neg(-2))#neagtive
#Write a program using map() and lambda function to double all elements in a list
li=[2,4,3,1]
ans=list(map(lambda x:x*2,li))
print(ans)#[4, 8, 6, 2]
#Write a program using map() and lambda function to find squares of all elements in a list.
li=[2,4,3,1]
square=list(map(lambda x: x*x,li))
print(square)#[4, 16, 9, 1]
#Write a program using filter() and lambda function to find even numbers from a list.
numbers=[1,4,2,7,8,9]
res=list(filter(lambda x: x%2==0,numbers))
print(res)#[4, 2, 8]
#Filter Odd Numbers
numbers=[1,4,2,7,8,9]
res=list(filter(lambda x: x%2!=0,numbers))
print(res)#[1, 7, 9]
#Write a program using filter() and lambda function to display numbers greater than 50.
numbers=[10,52,30,50,51,36,85,54,20,]
res=list(filter(lambda x:x>50,numbers))
print(res)#[52, 51, 85, 54]
#Write a program using filter() and lambda function to find palindrome words from a list.
li=["madam","sir","amma","hlelo","afifa","radar","level"]
ans=list(filter(lambda x:x==x[::-1],li))
print(ans)#['madam', 'amma', 'afifa', 'radar', 'level']