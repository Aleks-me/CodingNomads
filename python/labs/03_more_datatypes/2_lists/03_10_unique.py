'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

unique_list = []

for i in list_:
    how_much = list_.count(i)
    if how_much == 1:
        unique_list.append(i)

print(unique_list)
