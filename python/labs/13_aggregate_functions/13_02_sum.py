'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''

list_to_sum = [i for i in range(1, 11)]


def summ(i_list):
    cur = 0
    for pos in i_list:
        cur += pos
    return cur


print(summ(list_to_sum))
