'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

given_list = [n for n in range(1, 10000)]

gen = (x for x in given_list)
for elem in gen:
    if elem % 1111 == 0:
        print(elem)
