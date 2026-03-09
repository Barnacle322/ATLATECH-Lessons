# Простые типы данных
my_integer: int = 1  # Числовое значение
my_float: float = 5.3  # Десятичные дроби
my_string: str = "Arstan"  # Строковые значения
my_boolean: bool = False  # Булево значение


# Коллекции
my_list: list[int] = [1, 2, 3, 4]
my_tuple = ("arstan", "aliya", "Ulugbek")
my_set: set[float] = {5.5, 16.3, 8.7, 4.6}
my_dictionary: dict[str, int] = {"arstan": 22, "aliya": 21, "zhantai": 16}

my_list.append(5)
# print(my_tuple[2]) # Index


# Conditionals (Условные выражение)
password = "12"
correct_password = "123"

if password == correct_password:
    print("Yes, the pass is correct")
else:
    if len(password) > 3:
        print("The password is too long")
    elif len(password) < 1:
        print("The passowrd is too short")
    print("This pass is incorrect")

# == - Equals to
# > - More than
# < - Less than
# >= - More or equal to
# <= - Less or equal to

# Unpacking(распаковка)
first_variable, second_variable = 10, 20

# Loops(циклы)
for name, age in my_dictionary.items():
    if age > 18:
        print(f"{name} can vote")
    else:
        print(f"{name} can't vote")

counter = 0
while counter <= 10:
    print(counter)
    counter = counter + 1


# Functions(функции)
def check_voting_age(dictionary: dict[str, int]):
    for name, age in dictionary.items():
        if age > 18:
            print(f"{name} can vote")
        else:
            print(f"{name} can't vote")


check_voting_age(my_dictionary)
check_voting_age({"Ulugbek": 22, "Nursultan": 21, "Minar": 16})


def find_discriminant(a, b, c) -> float:
    discriminant = b**2 - 4 * a * c
    return discriminant


def number_of_solutions(discriminant: float) -> None:
    if discriminant > 0:
        print("2 solutions")
    elif discriminant == 0:
        print("1 solution")
    else:
        print("no solution")


discriminant = find_discriminant(3.3, 12.6, 5.2)
number_of_solutions(discriminant)


def name_printer(name_list: list, quantity: int) -> None:
    for name in name_list:
        counter = 0
        while counter < quantity:
            print(name)
            counter += 1


name_printer(["arstan", "aliya", "ulugbek"], 5)
