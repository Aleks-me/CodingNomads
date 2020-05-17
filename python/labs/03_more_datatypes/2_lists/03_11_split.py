'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

import re

word_bag = input("Please, enter some words or phrases: ")

w_list = re.split("\W", word_bag)

count_dict = {}

for word in w_list:
    counter = w_list.count(word)
    count_dict[word] = counter

count_dict = sorted(count_dict.items(), key=lambda kv: (kv[1], kv[0]))

print("\n")
print(f"Most word: {count_dict[-1][0]}, found {count_dict[-1][1]} times.")
