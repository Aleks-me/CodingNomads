'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

user_string = input("Please, type some words: ")
user_symbol = input("Please, enter symbol (e.g. #): ")

first_letter = user_string[0]

final_string = user_string.replace(first_letter, user_symbol)
final_string = final_string.replace(first_letter.lower(), user_symbol)

print(final_string)
