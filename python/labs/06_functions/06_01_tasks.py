'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
def div_4_or_7(number):
    if number % 4 == 0 or number % 7 == 0:
        return True
    else:
        return False

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean
def div_4_and_7(number):
    if number % 4 == 0 and number % 7 == 0:
        return True
    else:
        return False

# take in a number from the user between 1 and 1,000,000,000
user_input = int(input("""Please, enter the number \
between 1 and 1,000,000,000: """))

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 
first_result = div_4_or_7(user_input)
second_result = div_4_and_7(user_input)

# print your new variables to display the results
print("Divisible by 4 or 7?", first_result)
print("Divisible by 4 and 7?", second_result)
