#Using __str__() Method:
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def __str__(self):
        return f"Book: {self.title}, basics by {self.author}"
b1=Book("python","john")
print(b1)
#Modify properyies:
class Car:
    def set_details(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("The price of the car is:" ,self.price)
    def update_price(self,new_price):
        self.price=new_price
c1=Car()
c1.set_details("Ford",1000000)
c1.update_price(1500000)
c1.display()
#delete property:
class Person:
    def set_data(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("The Name: ",self.name)
        print("The age: ",self.age)
    def delete_age(self):
        del self.age
        #print("The age was deleted")
p1=Person()
p1.set_data("susmitha",20)
p1.display()
p1.delete_age()
#p1.display()
#problems on class properties:
#student school name:
class Student:
    school_name="Cambridge school"
    def set_data(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name: ",self.name)
        print("Marks: ",self.marks)
        print("school: ",self.school_name)
s1=Student()
s1.set_data("Susmitha",78)
s1.display()
#company employees:
class Employee:
    company="Infosys"
    def set_info(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Employee name: ",self.name)
        print("Employee Salary: ",self.salary)
        print("Employee company: ",self.company)
c1=Employee()
c1.set_info("Susmitha",1000000)
c1.display()
#changing class property:
class College:
    college_name="Chaitanya clg"
    def display(self):
        print("The old college is: ",College.college_name)
        self.college_name="Gurunanak clg"
        print("The new clg is: ",College.college_name)
c1=College()
c1.display()
#rate calculation:
class BankAccount:
    interest_rate=5
    def set_balance(self,balance):
        self.balance=balance
    def calculate_interest(self):
        interest=self.balance*self.interest_rate/100
        print("the interest is: ",interest)
b1=BankAccount()
b1.set_balance(200000)
b1.calculate_interest()