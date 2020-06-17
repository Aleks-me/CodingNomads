'''
Write a script with a function that demonstrates the use of *args.

'''


def like_eating(*args):
    for food in args:
        print(f"I like to eat {food}")


like_eating("pizza", "soup", "bread", "steak")

a_list = ["sausage", "cranberries", "tomatoes", "pilaf"]
like_eating(*a_list)
