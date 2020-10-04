'''
Write a script that generates an exception.
Handle this exception with a try/except.
For example:

list_ = ["hello world!"]
print(list_[1])

This raises and exception that needs to be handled.

'''
sequence = list(range(5))

try:
    sequence[6] = 10
except IndexError as ie:
    print(ie, f": list length = {len(sequence)}")
