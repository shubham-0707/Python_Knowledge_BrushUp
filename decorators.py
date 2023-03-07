# this program is made to demonstrate the functionality of decorators...

# We have to change the behaviour of our func function...
def func(a, b):
    print(a / b)


def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


func = smart_div(func)

func(5, 10)
