'''
Print out every prime number between 1 and 100.

'''

for val in range(2, 101):
    for n in range(2, val // 2 + 2):
        if (val % n) == 0:
            break
        else:
            if n == val // 2 + 1:
                print(val)
