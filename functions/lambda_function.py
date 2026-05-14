#lambda function:
'''lambda functions are anynomous function which means function without a name.Used for simple operations and written in a single line.'''
#squaring a number:
square=lambda x:x*x
print(square(5))#25
#cubing a number:
cube=lambda x:x**3
print(cube(4))#64
#adding of two same numbers:
add=lambda x:x+x
print(add(6))#12
#adding of two different numbers:
add=lambda x,y:x+y
print(add(2,3))#5
#multiplying numbers:
mul=lambda x,y:x*y
print(mul(2,5))#10
#lambda without arguments:
greet=lambda:"hey susmitha!"
print(greet())
#Lambda with Conditional Expression
largest=lambda a,b: a if a>b else b
print(largest(4,3))#4
#lambda function with higher order functions like :map(),reduce(),filter() etc.
'''lambda with map():
map() function applies condition to every element.'''
numbers=[1,4,3,2]
mul=list(map(lambda x: x*2,numbers))
print(mul)#[2 8 6 4]
#lambda with filter(): this function applies to elements based on the condition:
numbers=[1,3,4,2,6]
result=list(filter(lambda x:x%2==0,numbers))
print(result)#[4 2 6]
#lambda with sorted(): used for sorting.
li=[("ravi",20),("tharun",19),("rama",20)]
res=sorted(li,key=lambda x:x[1])
print(res)#[('tharun', 19), ('ravi', 20), ('rama', 20)]
li.sort(key=lambda x:x[1])
print(li)#[('tharun', 19), ('ravi', 20), ('rama', 20)]
li.sort(key=lambda x:x[0])
print(li)#[('rama', 20), ('ravi', 20), ('tharun', 19)]
#sorting based on length of words .
li=["susmitha","ravi","tharun","ramadevi"]
li.sort(key=lambda x:len(x))
print(li)#['ravi', 'tharun', 'susmitha', 'ramadevi']
#printing in descending order:
li.sort(key=lambda x:len(x),reverse=True)
print(li)#['susmitha', 'ramadevi', 'tharun', 'ravi']
#case sensitive:
li=["Susmitha","ravi","tharun","Ramadevi"]
li.sort(key=lambda x: x.lower())
print(li)#['Ramadevi', 'ravi', 'Susmitha', 'tharun']