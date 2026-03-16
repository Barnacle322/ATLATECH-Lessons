# Написание класса. Класс - это чертеж по которому можно создавать объекты
class User:
    # Аттрибуты
    id: int
    name: str
    age: int
    password: str
    email: str

    # Магический метод. Конструктор
    def __init__(self, id: int, name: str, age: int, pw: str, email: str):
        self.id = id
        self.name = name
        self.age = age
        self.email = email

        if len(pw) < 8:
            raise ValueError("Слшком короткий пароль")
        else:
            self.password = pw

    # Метод
    def login(self, password):
        if password == self.password:
            print("You have have logged in")
        else:
            print("Incorrect password")


# Инициализация класса -> объект -> экземпляр класса
arstan = User(1, "arstan", 22, "1234567890", "arstan@gmail.com")
ulugbek = User(2, "Ulugbek", 20, "987654321", "ulugbek@gmail.com")

# Вызов метода
arstan.login("1234567890")

# Обращение к аттрибуту
print(arstan.age)
