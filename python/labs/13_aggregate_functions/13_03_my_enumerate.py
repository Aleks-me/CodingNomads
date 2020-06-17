'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''
for_test = [n for n in range(1, 11)]


def my_enumerate(iterable):
    for i in range(len(iterable)):
        yield i, iterable[i]


print(list(my_enumerate(for_test)))
