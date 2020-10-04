'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''

inp1 = int(input("Enter starting number: "))
inp2 = int(input("Enter ending number: "))

sum_n = 0
for i in range(inp1, inp2+1):
    sum_n += i

print("Sum is:", sum_n)
