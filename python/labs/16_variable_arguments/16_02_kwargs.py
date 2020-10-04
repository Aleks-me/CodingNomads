'''
Write a script with a function that demonstrates the use of **kwargs.

'''


def like_eating(**kwargs):
    for suffix, food in kwargs.items():
        print(f"I like to eat {suffix} {food}")


like_eating(hot="pizza", chicken="soup", fresh="bread", well_done="steak")

a_dict = {"beef": "sausage", "jam": "cranberries",
          "yellow": "tomatoes", "Kazachstanian": "pilaf"}

like_eating(**a_dict)
