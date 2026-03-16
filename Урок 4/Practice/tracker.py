def add_expense(category: str, amount: float) -> None:
    with open("./Урок 4/Practice/expenses.txt", "a") as file:
        file.write(f"{category}:{amount}")


def load_expenses() -> list[tuple]:
    with open("./Урок 4/Practice/expenses.txt", "r") as file:
        return [tuple(line.replace("\n", "").split(":")) for line in file]


def expenses_by_category() -> dict[str, float]:
    expenses = load_expenses()
    categories = {}

    for category, amount in expenses:
        if category in categories.keys():
            categories[category] += float(amount)
        else:
            categories[category] = float(amount)

    return categories


def show_stats() -> None:
    expenses = expenses_by_category()
    if len(expenses) == 0:
        print("Расходов пока нет")

    for category, amount in expenses.items():
        print(f"{category}: {amount} сом")
    print("---")
    print(f"Итого: {sum(expenses.values())} сом")

    max_value_key = ""
    max_value = 0.0
    for category, amount in expenses.items():
        if amount > max_value:
            max_value_key = category
            max_value = amount

    print("Больше всего потрачено на: " + max_value_key)


while True:
    print("""
1 - Добавить расход
2 - Показать статистику
3 - Выйти
""")
    choice = input("Чо хотите: ")

    if choice == "1":
        category = input("Category: ")
        amount = float(input("Amount: "))
        add_expense(category=category, amount=amount)
    if choice == "2":
        show_stats()
    if choice == "3":
        break
