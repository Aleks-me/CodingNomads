'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

for tests:
    
1 2 9 8 5 6 0 3 7 12

1 2 9 8 5 6 0 3 7 

'''

num_str = input("Please, enter some numbers separated by space: ")

num_list = num_str.split()
num_list = list(map(int, num_list))

if len(num_list) % 2 == 0:
    tup_list = [(num_list[i],num_list[i+1]) for i in range(0,len(num_list),2)]
else:
    num_list.append(0)
    tup_list = zip(num_list[0::2], num_list[1::2])

print(*tup_list)
