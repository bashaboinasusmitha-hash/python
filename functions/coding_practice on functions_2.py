#User-defined Function Questions
'''Even or Odd'''
'''Write a user-defined function to check whether a number is even or odd.'''
def even_odd(number):
    if number%2==0:
        return ("number is even")
    else:
        return ("number is odd")
res=even_odd(7)
print(res)