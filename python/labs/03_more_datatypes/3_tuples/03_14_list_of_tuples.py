'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

import re

input_1 = input("Please, type some words: ")

list_w = re.split("\W+", input_1)

res_list = []
for word in list_w:
    tupl = tuple(word)
    res_list.append(tupl)

print("Words to tuple list:", res_list)
