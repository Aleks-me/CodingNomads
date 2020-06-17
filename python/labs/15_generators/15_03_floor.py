'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''

given_list = [n for n in range(1, 10000)]

gen = (x for x in given_list)
for elem in gen:
    print(elem // 1111)
