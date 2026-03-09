#class properties
'''properties are variables that belong to a class . 
They store data for each object created from the class'''
class Person:
    def __init__(self,name,age):#constructor is __init__,name,age are properties of an object
        self.name=name
        self.age=age
p1=Person("susmitha",20)#p1 is object
print(p1.name)
print(p1.age)
#Accessing the properties:
print(p1.name)
print(p1.age)
#Modify properties:
'''we can change the propertiess like name,age'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("susmitha",29)
print(p1.name)
print(p1.age)
p1.age=20#changing age 29 to 20
p1.name="Ramadevi"#changing name susmitha to Ramadevi
print(p1.name,p1.age)#here it prints like Ramadevi 20 instead of printing susmitha 29
#delete properties:
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("susmitha",26)
del p1.age
print(p1.name)#susmitha (this works )
#print(p1.age) this will give error because we have deleted the age
#class property VS instance property:
class Person:
    species="human"#class property
    def __init__(self,name):
        self.name=name
p1=Person("susmitha")
p2=Person("Ramadevi")
print(p1.name)
print(p2.name)
print(p1.species)
#modifying the class properties:
class Person:
    lastname=""
    def __init__(self,name):
        self.name=name
p1=Person("susmitha")
p2=Person("Ramadevi")
Person.lastname="Bashaboina"
print(p1.lastname)#bashaboina
print(p2.lastname)#bashaboina 
#Add new properties:
'''you can add new add properties to existing objects'''
class Person:
    def __init__(self,name):
        self.name=name
p1=Person("susmitha")
p1.age=20#adding age 
p1.city="Hanumakonda"#adding city
print(p1.name)
print(p1.age)
print(p1.city)
#Note: Adding properties this way only adds them to that specific object, not to all objects of the class.