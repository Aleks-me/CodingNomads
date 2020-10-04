'''
Demonstrate the use of the .enumerate() function.

'''

shopping_list = ["bread", "beans", "yoghurt", "sausages"]
for pos, item in enumerate(shopping_list, start=1):
    print(f"{pos}: {item}")
