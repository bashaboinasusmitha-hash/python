'''"Random Numbers": python does not have random() function to make random number,
but it has a built in module called"random" that can be used to make random numbers:'''
import random
#rando.randrange(a,b):it picks any number randomly from a<=x<b
print(random.randrange(1,10))
#random.randint(a,b):#prints any number including a and b
print(random.randint(1,10))
#random.random():its prints any floating numbers less than 1 
print(random.random())#(0.43863459279776695) 
#random.uniform(): it prints floating numbers but in range of specific numbers:
a=random.uniform(1,3)
print(a)#2.0892172673543357
#random.choice():it picks any value from a list
li=[1,2,-4,10,3,"susmitha"]
a=random.choice(li)
print(a)
print(random.choices(li,k=3))#[3, 10, 3]
#random.shuffle():it will change the order of list
li=[1,2,-4,10,3,"susmitha"]
random.shuffle(li)
print(li)
#generating multiple random numbers :
print(random.sample(range(1,20),5))#[9, 13, 2, 19, 15]
#if we want same random numbers every time (for testing)
print(random.seed(10))