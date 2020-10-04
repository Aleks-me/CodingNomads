'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

number = int(input("Enter number between 1 and 1,000,000,000: "))

result = number / 3

if number % 3 == 0:
    print("Fully divisible by 3! -", result)
else:
    print("Not divisible by 3, there's remainder -", result)
