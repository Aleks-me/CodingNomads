'''
Write a decorator function that wraps text passed to it in a html <p> tag.

'''


def decorator(func):
    def wrapper(msg):
        return f"<p>{func(msg)}<p>"
    return wrapper


@decorator
def texting(msg):
    return msg


print(texting("When you see it - you shit bricks!"))
