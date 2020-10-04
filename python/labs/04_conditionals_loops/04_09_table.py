'''
Use a loop to print the following table to the console:

 0 1 2 3 4 5 6 7 8 9
 10 11 12 13 14 15 16 17 18 19
 20 21 22 23 24 25 26 27 28 29
 30 31 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47 48 49

'''

c_row = 0
while c_row < 5:
    st = ""
    c_num = 0
    while c_num < 10:
        if c_row == 0:
            st += str(c_num) + " "
        else:
            st += str(c_row) + str(c_num) + " "
        c_num += 1
    print(st)
    c_row += 1
