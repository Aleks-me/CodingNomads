'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

input_1 = input("Please, enter first word: ")
input_2 = input("Please, enter second word: ")
input_3 = input("Please, enter last word: ")

print("\n")

print(str(len(input_1)) + ",", input_1)
print(str(len(input_2)) + ",", input_2)
print(str(len(input_3)) + ",", input_3)

# part for challenge:
print("\n")
input_list = []
input_list.append(len(input_1))
input_list.append(len(input_2))
input_list.append(len(input_3))

if max(input_list) == len(input_1):
    print(str(len(input_1)) + ",", input_1)
elif max(input_list) == len(input_2):
    print(str(len(input_2)) + ",", input_2)
else:
    print(str(len(input_3)) + ",", input_3)
