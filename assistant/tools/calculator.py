def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"


def calculate() -> None:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    operation = input("Выберите операцию (+, -, *, /): ")

    result = ""
    try:
        if operation == "+":
            result = add(a, b)
        elif operation == "-":
            result = subtract(a, b)
        elif operation == "*":
            result = multiply(a, b)
        elif operation == "/":
            result = divide(a, b)
        else:
            raise ValueError
    except ValueError:
        print("Неверные входные данные")

    print(f"Результат: {result}")
