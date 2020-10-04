'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''
path = "/home/alex_me/Documents/CodingNomads/python/labs/09_exceptions/books/"

files = ["war_and_peace.txt",
         "crime_and_punishment.txt",
         "pride_and_prejudice.txt"]

try:
    with open(path + files[0]) as wap:
        book_1 = wap.read()
    with open(path + files[1], "w") as cap:
        cap.write("")

    for file in files:
        with open(path + file) as book:
            string = book.readline()
            if len(string) != 0:
                print(string[1])
            else:
                print("")
except IOError as io:
    print(io)
except PermissionError as pe:
    print(pe)
except IndexError as ie:
    print(ie)


# Challenge section
class FindPrince(Exception):
    def __init__(self, message):
        self.message = message


for file in files:
    with open(path + file) as book:
        string = ""
        while len(string) < 100:
            string += book.readline()
        print(string)
        if "Prince" in string:
            raise FindPrince("Prince here!")
