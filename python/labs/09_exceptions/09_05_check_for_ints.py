'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''
while True:
    inp = input("Enter some number to check it's an integer: ")

    try:
        print(f"{int(inp)} is an integer.")
    except ValueError:
        print("Your input is not an integer. Bye!")
        break
