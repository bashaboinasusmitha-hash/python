#Challenge: self Parameter
class Car:
    def __init__(self,brand):
        self.brand=brand
    def show(self):
        print(self.brand)
c1=Car("Ford")
c1.show()
#Challenge: Class Properties
class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
s1=Student("Anna","A")
print(s1.grade)
s1.grade="B"
print(s1.grade)