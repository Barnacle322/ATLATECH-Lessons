class Animal:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} лет"

    def speak(self) -> None: ...


class Dog(Animal):
    type: str

    def __init__(self, name, age, type):
        super().__init__(name, age)
        self.type = type

    def speak(self) -> None:
        print(f"Гав! Меня зовут {self.name} и я {self.type} собака")


class Cat(Animal):
    breed: str

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self) -> None:
        print(f"Мяу! Меня зовут {self.name} и я {self.breed} кошка")


# Проверь себя:
# dog = Dog("Бубик", 28, "Декоративная")
# print(dog)  # Бубик, 28 лет
# dog.speak()  # Гав! Меня зовут Бубик

# Проверь себя:
# cat = Cat("Барсик", 3, "Сиамская")
# print(cat)
# cat.speak()


animals = [
    Animal("Животное", 1),
    Dog("Бубик", 28, "Декоративная"),
    Cat("Барсик", 3, "Сиамская"),
]

for animal in animals:
    animal.speak()
