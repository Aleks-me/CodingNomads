'''
Write a script that reads in the words from the words.txt file and finds
and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''

list_of_words = []
with open("words.txt") as words_f:
    for word in words_f.readlines():
        list_of_words.append(word.rstrip())

shortest = []
longest = []
min_w = min(list_of_words, key=len)
max_w = max(list_of_words, key=len)

for s in list_of_words:
    if len(s) == len(min_w):
        shortest.append(s)
    elif len(s) == len(max_w):
        longest.append(s)

# Output:
print(f"Shortest words: max {len(min_w)} chars.")
for sw in shortest:
    print(sw)

print("\n")
print(f"Longest words: max {len(max_w)} chars.")
for lw in longest:
    print(lw)

print("\n")
print("Amount of words: ", len(list_of_words))
