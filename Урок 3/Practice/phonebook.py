def add_contact(name: str, phone: str) -> None:
    with open("./Урок 3/Practice/contacts.txt", "a") as file:
        file.write(f"{name}:{phone}\n")


def load_contacts() -> dict[str, str]:
    with open("./Урок 3/Practice/contacts.txt", "r") as file:
        my_dict = {}
        for line in file:
            name, phone = line.replace("\n", "").split(":")
            my_dict[name] = phone

        return my_dict


def find_contact(name: str) -> None:
    contacts = load_contacts()
    print(contacts[name])


def list_contacts() -> None:
    contacts = load_contacts()

    validated_contacts = [
        phone for phone in contacts.values() if phone.startswith("+996")
    ]
    print(
        "Телефонная книга пуста" if len(validated_contacts) == 0 else validated_contacts
    )


while True:
    print("""
1 - Добавить контакт
2 - Найти контакт
3 - Показать все контакты
4 - Выйти
""")
    choice = input("Чо хотите: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        add_contact(name, phone)
    if choice == "2":
        name = input("Name: ")
        find_contact(name)
    if choice == "3":
        list_contacts()
    if choice == "4":
        break
    else:
        raise ValueError("Неправильные входные данные")
