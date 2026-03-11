class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
r1=Rectangle(5,3)
print("Area is:",r1.area())
#employee salary update:
class Employee:
    def set_info(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Employee Name:", self.name)
        print("Salary:" ,self.salary)
    def increase_salary(self,amount):
        self.salary+=amount
e1=Employee()
e1.set_info("Susmitha",30000)
e1.increase_salary(5000)
e1.display()
#Bank Account:
class BankAccount:
    def create_account(self,name,balance):
        self.name=name
        self.balance=balance
    def display(self):
        print("Balance:" ,self.balance)
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
b1=BankAccount()
b1.create_account("susmitha",3000)
b1.deposit(2000)
b1.withdraw(500)
b1.display()
#Calculator class:
class Calculator:
    def add(self,a,b):
        print("Sum =",a+b)
    def subtract(self,a,b):
        print("Difference =",a-b)
    def multiply(self,a,b):
        print("Product =",a*b)
    def divide(self,a,b):
        print("Quotient =",a//b)
c1=Calculator()
c1.add(6,4)
c1.subtract(6,2)
c1.multiply(3,7)
c1.divide(4,2)
#student details:
class Student:
    def set_data(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name:" ,self.name)
        print("Marks:" ,self.marks)
s1=Student()
s1.set_data("Susmitha",85)
s1.display()