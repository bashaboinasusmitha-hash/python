#Convert the temperature:
'''You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.
You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].
Return the array ans. Answers within 10-5 of the actual answer will be accepted.'''
celsius=122.11
kelvin=celsius+273.15
fahreinheit=celsius*1.80+32.00
res=[kelvin,fahreinheit]
print(res)