# Аттрибут по умолчанию(Default argument)
def greet(name: str, greetings: str = "Salam Aleikum") -> str:
    return f"{greetings}, {name}"


# print(greet("Zhantai"))
# print(greet("Adilet", "Hello"))


# Позиционные аргменты и keyword аргументы
def find_discriminant(a, b, c) -> float:
    discriminant = b**2 - 4 * a * c
    return discriminant


print(find_discriminant(10, 20, 30))
print(find_discriminant(10, 20, c=30))
print(find_discriminant(10, 20, 30))
