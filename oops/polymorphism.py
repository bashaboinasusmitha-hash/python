#Python Polymorphism:
'''The word polymorphism refers to many "forms",and in programming it refers to
 methods or  functions or operations with the same name that can be executed on many objects or classes'''
#function Polymorphism:
'''an example of a python function that can be used on different objects is "len().function'''
#strings:for strings len() returns the number of characters
x="Hello World"
print(len(x))#11
#tuple:for tuples len() function returns the number of items in tuple
t=(1,2,3,7,1)
print(len(t))#5
#Dictionary:for dictionaries it returns number of key value pairs in dictionary
dic={"Name":"Susmitha","Age":20,"course":"B-Tech"}
print(len(dic))#3
#Class Polymorphism:
'''Polymorphism is often used in Class methods where we can have multiple classes with 
the same method name ex:we have 3 classes :Car,Boat,Plane and they have a method called move()'''
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Drive")
class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Sail!")
class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Fly!")
c1=Car("Ford","Mustang")
b1=Boat("Ibiza","Touing 20")
p1=Plane("Boeing","747")
for x in (c1,b1,p1):
    x.move()
c1.move()
b1.move()
p1.move()
#inheritance Class Polymorphism:
class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Move!")
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def move(self):
        print("go!")
class Boat(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def move(self):
        print("Sail!")
class Plane(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand,model)
    def move(self):
        print("Fly!")
c1=Car("Ford","Mustang")
b1=Boat("Ibiza","Touing 20")
p1=Plane("Boeing","747")
for i in (c1,b1,p1):
    i.move()