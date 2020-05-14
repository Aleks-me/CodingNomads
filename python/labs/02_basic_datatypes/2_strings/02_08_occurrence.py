'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

user_words = input("Please, type some words: ")
user_letter = input("Please, enter some letter (e.g. h): ")

finder = user_words.find(user_letter)

print(finder)
