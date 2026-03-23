from datetime import datetime


class Product:
    # Аттрибуты -> То как оьъекты могут быть описаны
    name: str
    release_date: datetime
    description: str
    price: float
    # Private attribute(Приватный аттрибут)
    __stock: int = 0

    # Методы -> то, что объекты могут делать

    # Конструктор(магический метод) (d(ouble)under(score) method)
    def __init__(self, name, release_date, description, price):
        self.name = name
        self.release_date = release_date
        self.description = description

        if price < 1:
            raise ValueError("Нельзя поставить такую цену")
        self.price = price

    # Getter
    def get_stock(self):
        return self.__stock

    # Setter
    def set_stock(self, amount):
        if amount < 1 or amount > 100000:
            raise ValueError("Неверное значение инвентаря")

        self.__stock = amount

    def sell(self, amount=1):
        if amount < 1 or amount > 100000:
            raise ValueError("Неверное значение инвентаря")
        if amount > self.__stock:
            raise ValueError("Не хватает инвентаря")

        self.__stock -= amount


# создание объекта(инстанциирование класса|создание экземпляра класса)
iphone_17 = Product(
    name="iPhone 17 Pro Max",
    release_date="2025",
    description="Best phone in the galaxy(maybe)",
    price=1499.0,
)

iphone_16 = Product(
    name="iPhone 16 Pro Max",
    release_date="2024",
    description="Second best phone in the galaxy(maybe)",
    price=1399.0,
)

# Вызов методов
iphone_16.set_stock(1000)
print(iphone_16.get_stock())
iphone_16.sell()
print(iphone_16.get_stock())
