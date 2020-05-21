'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''

n = 3
x = 0
while x < n:
    print("*" + "*" * x)
    x += 1
