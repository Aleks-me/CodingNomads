'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
test_list = [2, 8, 16, 8, 2]
length = 10


def gen_list(n):
    list_gen = [x for x in range(0, n)]
    return list_gen


middle_list = gen_list(10)


def add_to_list(test, addd):
    big_list = test + addd
    return big_list


for_print_list = add_to_list(test_list, middle_list)


def elem_list(inp):
    inp.sort()
    return print(inp)


elem_list(for_print_list)
