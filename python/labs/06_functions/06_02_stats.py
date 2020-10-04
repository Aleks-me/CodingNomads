'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(list_numbers):
    # define the function here
    max_l = max(list_numbers)
    min_l = min(list_numbers)
    avg_l = len(list_numbers) / 2
    sum_l = sum(list_numbers)
    return max_l, min_l, avg_l, sum_l

# call the function below here
print(stats(example_list))
