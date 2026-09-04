import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
dic={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":division
}
def calculator():
    num1=float(input("Enter the first number:"))
    for symbol in dic:
        print(symbol)
    continue_flag=True
    while continue_flag:
        operation_sym=input("Enter the operation symbol:")
        num2=float(input("Enter the second number:"))
        calculation=dic[operation_sym]
        result=calculation(num1,num2)
        print(f"{num1} {operation_sym} {num2} = {result}")
        should_continue=input(f"Enter 'y' to continue {result} or 'n' to start new calculation or 'x' to exit:").lower()
        if should_continue=="y":
            num1=result
        elif should_continue=="n":
            continue_flag=False
            os.system("cls")
            calculator()#recursion(function inside the function)
        else:
            continue_flag=False
            print("BYE")
calculator()