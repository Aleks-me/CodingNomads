'''
Write a script that reads in the contents of words.txt and writes the contents
in reverse to a new file words_reverse.txt.
'''

list_of_words = []
with open("words.txt") as words_f:
    for word in words_f.readlines():
        list_of_words.append(word)

list_of_words = list_of_words[::-1]

with open("words_reverse.txt", "w") as words_r:
    words_r.write("".join(list_of_words))


# Let's see what we've got:
with open("words.txt") as words_10:
    print("Before:")
    for line in range(10):
        print(words_10.readline().rstrip())

with open("words_reverse.txt") as r_words_10:
    print("\n")
    print("After:")
    for line in range(10):
        print(r_words_10.readline().rstrip())
