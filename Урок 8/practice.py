# Блок 1
# imya = input("Введите имя: ")
# vozrast = 22
# rost = 1.75
# is_student = False

# print(f"Меня зовут {imya}, мне {vozrast} года, мой рост {rost}м, студент {is_student}")
# print(f"{imya.upper()} -  {len(imya)} символов")

# Блок 2

# user_int = int(input("Введите число: "))
# if user_int % 2 == 0:
#     print("четное")
# else:
#     print("нечетное")

# Range(start, stop, step)
# start - то с чего начинаем(инклюзивно)
# stop - то с чем заканчиваем(эклюзивно)
# step - шаг
# for i in range(1, 21):
#     if i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)


# tries = 3
# password = "qwerty123"
# while tries >= 0:
#     user_input = input("Введите пароль: ")
#     if user_input == password:
#         print("Добро пожаловать")
#         break
#     else:
#         if tries >= 1:
#             print(f"Неверно, осталось {tries} попытки")
#             tries -= 1
#         else:
#             print("Аккуант заблокирован")
#             break

# Блок 3
# def is_even(number: int) -> bool:
#     if number % 2 == 0:
#         return True
#     else:
#         return False


# print(is_even(4))  # True
# print(is_even(7))  # False


def clamp(value: int, min_val: int, max_val: int) -> int:
    if value < min_val:
        return min_val
    if value > max_val:
        return max_val
    return value


# print(clamp(15, 0, 10))  # 10
# print(clamp(-5, 0, 10))  # 0
# print(clamp(7, 0, 10))  # 7

# Блок 4

# grades = [85, 42, 91, 58, 73, 66]
# print(round(sum(grades) / len(grades)))
# print(max(grades))
# print(min(grades))

# people = {"арстан": 22, "алия": 21, "жантай": 16}
# old_people = {name: age for name, age in people.items() if age > 16}


# words = ["привет", "мир", "python", "код", "класс"]
# new_words = [word.upper() for word in words if len(word) > 4]
# print(new_words)


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Ошибка деления на ноль")
    except TypeError:
        print("Ошибка: некорректный тип данных")
    except Exception:
        print("Неизвестная ошибка")


# safe_divide(10, 2)  # 5.0
# safe_divide(10, 0)  # "Ошибка: деление на ноль"
# safe_divide(10, "a")  # "Ошибка: некорректный тип данных"


# try:
#     with open("./Урок 8/notes.txt", "r") as file:
#         for row in file:
#             print(row.replace("\n", " "), end="")
# except Exception:
#     print("Файл не найден")


class Rectangle:
    width: int
    height: int

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * self.width + 2 * self.height

    def __str__(self):
        return f"Прямоугольник {self.width}x{self.height} | Площадь: {self.area()} | Периметр: {self.perimeter()}"


rect = Rectangle(10, 20)
print(rect)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(w=side, h=side)


sq = Square(10)
print(sq)
