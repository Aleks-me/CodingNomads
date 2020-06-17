'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

numbers = list(range(1, 11))
result = {}
for i in numbers:
    result[i] = i*i

# result = {x: x*x for x in range(1, 11)}

print(result)
