'''
Write a script that demonstrates a try/except/else.

'''

try:
    file = open("integers.txt")
    for line in file.readlines():
        print(line.rstrip())
except IOError:
    print("There is no such file.")
else:
    print("Reading complete, closing file...")
    file.close()
