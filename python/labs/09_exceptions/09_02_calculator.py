'''
Write a script that takes in two numbers from the user
and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''

inp_1 = input("Enter the first number: ")
inp_2 = input("Enter the second number: ")

try:
    print("Division result: ", float(inp_1) / float(inp_2))
except ValueError as ve:
    print(ve, ": use only numbers!")
except ZeroDivisionError as zde:
    print(zde, ": second number must not be zero!")
