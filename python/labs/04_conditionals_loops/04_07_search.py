'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

inp_num = int(input("Enter the number between 0 and 1,000,000,000: "))

finder = 0
while finder != inp_num:
    finder += 1

print("Number found, it's:", finder)
