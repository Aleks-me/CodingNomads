'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

list_of_words = []
with open("words.txt") as words_f:
    for word in words_f.readlines():
        list_of_words.append(word.rstrip())

longest = []
for w in list_of_words:
    if len(w) >= 21:
        longest.append(w)

# Output:
print("Words with more than 20 characters:")
for lw in longest:
    print(lw + ", length:", len(lw))
