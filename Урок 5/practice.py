class BankAccount:
    owner: str
    # Private attribute(приватные аттрибуты) не могут быть вызваны вне контекста класса
    __balance: float = 0.0
    __transaction_list: list[str] = []

    def __init__(self, owner):
        self.owner = owner

    def __str__(self):
        return f"{self.owner} has {self.__balance}"

    # def __repr__(self):
    #     return f"{self.owner} has {self.__balance}"

    def add_money(self, amount):
        if amount <= 0:
            raise ValueError("низя")

        self.__balance += amount
        self.__transaction_list.append(f"added {amount}")

        with open(file=f"./Урок 5/{self.owner}.txt", mode="a") as file:
            file.write(f"added {amount}\n")

    def remove_money(self, amount):
        if amount <= 0:
            raise ValueError("низя")

        if amount > self.__balance:
            raise ValueError(f"ты бедный tebe nuzhno: {amount - self.__balance}")

        self.__balance -= amount
        self.__transaction_list.append(f"removed {amount}")
        with open(file=f"./Урок 5/{self.owner}.txt", mode="a") as file:
            file.write(f"remove {amount}\n")

    def print_transactions(self):
        with open(file=f"./Урок 5/{self.owner}.txt", mode="r") as file:
            for index, element in enumerate(file, start=1):
                print(index, element, end="")

    def bank_statement(self):
        with open(file=f"./Урок 5/{self.owner}.txt", mode="r") as file:
            balance = 0.0
            for transaction in file:
                try:
                    action, amount = transaction.split()
                    if action == "added":
                        balance = balance + float(amount)
                    elif action == "remove":
                        balance = balance - float(amount)
                except Exception:
                    pass

            return balance


new_account = BankAccount(owner="Arstan")
print(new_account.bank_statement())
