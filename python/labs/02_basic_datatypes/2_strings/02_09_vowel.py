'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

user_input = input("Please, type one or several words: ")

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

how_much = 0
for v in vowels:
    # comment lines 17, 18 for challenge:
    counts = user_input.count(v)
    how_much += counts
    
# =============================================================================
#     # uncomment this for challenge:
#     if v in user_input:
#         how_much += 1
# =============================================================================
    
print("Total vowels in your words:", how_much)
