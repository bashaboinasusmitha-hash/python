'''logical operators generally returns True or False.The logical operators are : and,or,not.
and: the and returns True only if both conditions are True.T,T->T,if anything else->F
or:the or returns True if any one of the condition is True.T,F OR F,T OR T,T->T,if anything else False
not: it reverse the results'''
#and operator:
a=int(input("Enter any number:"))
b=int(input("Enter sny number:"))
print(a>20 and b<10)
#or operator
print(a>20 or b<10)
#not operator
print(not(a<b))
print(not(a))
c,d=4,3
print(not(a))
c=False
print(not(c))
'''Advanced concepts:Short-Circuiting
logical operators not always print True or False '''
print(10 and 20)
print(0 and 20)
print(0 or 10)
print(10 or 20)
'''in this type of cases the output is decided by using rules of 'or', 'and' 
0->false
any non zero integer tends to True  values
Rule of 'and'
and->returns first false value or last value if both the values are true
for example:'''
print(10 and 20)#it returns 20 because both values are true
print(0 or 20)#it returns 0 because and finds the first false value 
#Rule of 'or'
#or returns first true value
print(10 or 20)#it returns 10 because it stops checking when it finds non zero number at first
print(0 or 20)#it returns 20 because it finds True values first
#operator precedence:
print("the order of execution is:not,and,or")
#example:
print(True or False and False)#here it solves first 'and' after 'or'