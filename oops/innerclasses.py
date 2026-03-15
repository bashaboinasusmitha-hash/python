#Inner Classes:
'''An inner class is defined inside the another class.The inner class can access the 
properties and methods of outer class.
Inner classes are useful for grouping classess that are only used in one place,making 
code more organized .'''
class Outer:
    def __init__(self):
        self.name="Outer class"
    class Inner:
        def __init__(self):
            self.name="Inner Class"
        def display(self):
            print("This is inner class")
outer=Outer()
print(outer.name)
#Accessing the inner class from outside:
'''to access the inner class from outside of class we need to create an object for outer class and inner class
and need to write:Outerclass.Innerclass()'''
class Outer:
    def __init__(self):
        self.name="Outer class"
    class Inner:
        def __init__(self):
            self.name="Inner class"
        def display(self):
            print("This is an inner class")
outer=Outer()# outer class object
print(outer.name)#Outer class
inner=Outer.Inner()#inner class object
inner.display()# it shows "This is an inner class" 
#Accessing Outer Class from inner class:
'''inner classes in python do not automatically have access to the outer class instance.
if we want the inner class to access the outer class,you need to pass the outer class instance as a parameter'''
class Outer:
    def __init__(self):
        self.name="Susmitha"
    class Inner:
        def __init__(self,outer):
            self.outer=outer
        def display(self):
            print(f"The Outer class name : {self.outer.name}")
outer=Outer()
inner =outer.Inner(outer)
inner.display()
#Practical Example:
'''inner classes are useful for creating helper classes that are only used
within the context of the outer class:'''
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        self.engine=self.Engine()#object of inner class
    class Engine:
        def __init__(self):
            self.status="off"
        def start(self):
            self.status="Running"
            print("Engine started")
        def stop(self):
            self.status="off"
            print("Engine stopped")
    def drive(self):
        if self.engine.status=="Running":
            print("Driving the ",self.brand,self.model)
        else:
            print("Start the engine first!")
c1=Car("Toyoto","Corolla")
c1.drive()#start the engine first!
c1.engine.start()#this turns the status to "Running"
c1.drive()#Driving the Toyoto Corolla
'''when we create an object for outer class it following happens automatically:
brand:Toyoto
model:Corolla
engine.stautus:off'''#this because we created a inner object at outer constructor so automatically inner class constructor runs
'''so again by c1.engine.start() the status of engine turns to "Running'''
#Multiple inner classes: a class can have multiple classes:
class Computer:
    def __init__(self):
        self.cpu=self.CPU()
        self.ram=self.RAM()
    class CPU:
        def process(self):
            print("Processing the data....")
    class RAM:
        def store(self):
            print("Storing the data....")
com=Computer()
com.cpu.process()
com.ram.store()