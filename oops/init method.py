#the_init_()method
'''All classes have a built-in method called _init_(),which is always executed when the class is being initiated.
The _init_() is used to assign values to object properties,or to perform operations
that are neccessary when the object is being created'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("susmitha",20)
print(p1.name)
print(p1.age)
#Why use _init_()?
'''without the _init_() we need to set properties manually for each objet'''
class Person:
    pass
p1=Person()
p1.name="susmitha"
p1.age=20
print(p1.name)
print(p1.age)
#default values in _init_():
'''you can also set default values for parameters in the _init_()'''
class Person:
    def __init__(self,name,age=18):
        self.name=name
        self.age=age
p1=Person("susmitha")
p2=Person("ravinder",30)
print(p1.name,p1.age)#susmitha 18(bydefault it value from argument)
print(p2.name,p2.age)#ravinder 30
class Person:
    def __init__(self,name,age=18):
        self.name=name
        self.age=age
p1=Person("susmitha")
p2=Person("ravinder")
print(p1.name,p1.age)#susmitha 18(bydefault it value from argument)
print(p2.name,p2.age)#ravinder 18
class Person:
    def __init__(self,name,age=18):
        self.name=name
        self.age=age
p1=Person("susmitha",30)
p2=Person("ravinder")
print(p1.name,p1.age)#susmitha 30
print(p2.name,p2.age)#ravinder 18(bydefault it value from argument)      
#multiple parameters:
'''the _init_() can have as many as parameters as we need'''
class Person:
    def __init__(self,name,age,city,country):
        self.name=name
        self.age=age
        self.city=city
        self.country=country
p1=Person("susmitha",20,"hanumakonda","India")
print(p1.name,p1.age,p1.city,p1.country)#susmitha 20 hanumakonda India
print(p1.name)#susmitha
print(p1.age)#20
print(p1.city)#hanumakonda
print(p1.country)#India