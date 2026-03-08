class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print(self.name + "say woof!")
d1=Dog("Buddy",3)
print(d1.name,d1.age)
d1.bark()
#greet code challenge:
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print("hello my name is" +" " + self.name)
p1=Person("John",36)
print(p1.name,p1.age)
p1.greet()