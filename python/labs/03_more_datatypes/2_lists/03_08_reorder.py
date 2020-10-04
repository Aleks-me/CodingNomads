'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

print("Please, enter 10 numbers one by one.")

list_numbers_2 = []

for i in range(1, 11):
    one_digit = int(input(f"Please, enter {i} number: "))
    list_numbers_2.append(one_digit)

rev_list = []

for even in list(range(1, 10, 2)):
    rev_list.append(list_numbers_2[even])

for odd in reversed(list(range(0, 9, 2))):
    rev_list.append(list_numbers_2[odd])

print("\n")
print(rev_list)
