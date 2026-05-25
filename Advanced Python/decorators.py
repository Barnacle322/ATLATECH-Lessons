# 1. Функции - это объекты
# def greet():
#     print("Hello world")


def run(func):
    func()


# run(greet)


# 2. Функция может быть в функции
def outer():
    def inner():
        print("Внутри")

    def inner_second():
        print("second")

    inner()


# outer()

# Декоратор


# def my_decorator(func):
#     def wrapper():
#         print("Before")
#         func()
#         print("after")

#     return wrapper


# def greet():
#     print("Hello world")


# greeting = my_decorator(greet)
# greeting()

# Синтаксис @


def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("after")

    return wrapper


@my_decorator
def greet():
    print("Hello world")


greet()
