def decor(func):
    def wrapper(*args):
        print('Внутри декоратора')
        func(*args)
    return wrapper


# @decor
# def foo():
#    print('Внутри функции')


# foo()

def foo():
    print('Внутри функции')


foo = decor(foo)

foo()
