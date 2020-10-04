'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''


def decorator_tag(tag):
    def decorator(func):
        def wrapper(msg):
            return f"{tag}{func(msg)}{tag}"
        return wrapper
    return decorator


@decorator_tag("<old_memes>")
def texting(msg):
    return msg


print(texting("When you see it - you shit bricks!"))
