def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)


def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner


# lambda is anonymous single line function
# mainly used inside map and filter function
a = [1, 2, 3, 4, 5, 6]
newList = list(map(lambda x: x+5, a))
print(newList)


evenList = list(filter(lambda x: x % 2 == 0, a))
print(evenList)
