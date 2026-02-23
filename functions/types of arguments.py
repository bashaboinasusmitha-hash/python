'''there are mainly four types of functions with arguments they are:
 default,keyword,positional,arbitary/variable length'''
#positional arguments:
''' arguments are passed in correct order. Order must match the parameters
if order changes - results changes'''
def student(name,age):
    print("hello",name)#hello susmitha
    print("i'm",age,"years old")#i'm 20 years old
student("susmitha",20)
#here in place of name it taken 20 and in place of age it taken susmitha so the meaning was changed
def student(name,age):
    print("hello",name)#hello 20
    print("i'm",age,"years old")#i'm susmitha years old
student(20,"susmitha")
#keyword arguments:
'''arguments are passed using parameter name.Order does not matter,more redable'''
def student(name,age):
    print("hello",name)#hello susmitha
    print("i'm", age ,"years old")#i'm susmitha years old
student(age=20,name="susmitha")
def student(name,age):
    print("hello",name)#hello susmitha
    print("i'm", age ,"years old")#i'm susmitha years old
student(name="susmitha",age=20)
def student(name,age):
    print("hello",name)#hello susmitha
    print("i'm", age ,"years old")#i'm susmitha years old
student("susmitha",age=20)
'''f we write as student(age=20,"susmitha") then it will error 
because keyword arguments must follow positional arguments'''
#here we have written first age and then name but the meaning is not changed as before in postional arguments
#order is changed but output is correct
#Default arguments:
'''here parameter has a default value.if user doesnot pass any value default is used
if value is passes default is replaced'''
def greet(name,subject,dept="csm"):
    print(f"hii {name}")#hi susmitha 
    print(f"do u teach {subject} ?")#do u teach python ?
    print(f"are u from {dept} ?")#are u from csm ?
greet("susmitha","python")
#bydefault here at department it takes csm without passing argument again 
def greet(name,subject,dept="csm"):
    print(f"hii {name}")#hi susmitha 
    print(f"do u teach {subject} ?")#do u teach python ?
    print(f"are u from {dept} ?")#are u from cse ?
greet("susmitha","python","cse")
#here if we write like below it shows error like:parameter without a default follows parameter with a default
'''def greet(name,subject="python",dept):
    print(f"hii {name}") 
    print(f"do u teach {subject} ?")
    print(f"are u from {dept} ?")
greet("susmitha","cse")#parameter without a default follows parameter with a default'''
#so by default value must be at last
def greet(name,dept,subject="python"):
    print(f"hii {name}")#hi susmitha 
    print(f"do u teach {subject} ?")#do u teach python ?
    print(f"are u from {dept} ?")#are u from cse ?
greet("susmitha","cse")
#Arbitary arguments:
'''used when number of arguments is unknown 
*args stores values in tuples,can pass multiple values'''
def add(*numbers):
    print(numbers)#(1, 2, 3, 4)
    print("Sum",sum(numbers))#Sum 10
add(1,2,3,4)
def add(*numbers):
    c=0
    for i in numbers:
        c+=i
    print(f"The sum is {c}")#The sum is 24
add(13,8,3)
#*-used for positional arguments:
#**-used for arbitary keyword arguments
def add(*numbers,name):
    c=0
    print(numbers)#(12,2,5)
    print(name)#susmitha
    for i in numbers:
        c+=i
    print(c)#19
add(12,2,5,name="susmitha")
#if we write like below it show error as :(add() missing 1 required keyword-only argument: 'name)
'''def add(*numbers,name):
    c=0
    print(numbers)
    print(name)
    for i in numbers:
        c+=i
    print(c)
add(12,2,5)'''
#here in below code it taking name as 12 and numbers as (2,7)
def add(name,*numbers):
    c=0
    print(numbers)#(2, 5)
    print(name)#12
    for i in numbers:
        c+=i
    print(c)#7
add(12,2,5)
#**kwags:
def info_person(**kwags):
    for key,value in kwags.items():
        print(key,value)
info_person(name="susmitha",age=20,dept="csm")
#the output:
'''name susmitha
age 20
dept csm'''
#if we write as below code it will give error becuse always the *args should before **kwags
'''def info_person(**kwags,*args):
    for key,value in kwags.items():
        print(key,value)
    print(args)
info_person(name="susmitha",age=20,dept="csm")'''
def info_person(*args,**kwags):
    for key,value in kwags.items():
        print(key,value)
    print(args)#(1,2)
info_person(1,2,name="susmitha",age=20,dept="csm")
#the output is
'''name susmitha
age 20
dept csm
(1, 2)'''