'''
Demonstrate how to create a generator object. Print the object to
the console to see what you get.
Then iterate over the generator object and print out each item.

'''
print((x for x in range(10)))

gen = (x for x in range(10))
for i in gen:
    print(i)
