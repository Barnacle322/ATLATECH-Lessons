from tools import info, notes
from tools.calculator import calculate


def menu():

    user_input = input("""
Добрый день, Арстан!

Выберите раздел:
1 - Калькулятор
2 - Заметки
3 - Информация
4 - Выйти
\n
""")

    if user_input == "1":
        calculate()
    if user_input == "2":
        notes_input = input("""
1 - Добавить заметку
2 - Показать все заметки
3 - Найти заметку
4 - Выйти
""")
        if notes_input == "1":
            text_input = input("введите заметку: ")
            notes.add_note(text_input)
        elif notes_input == "2":
            notes.show_notes()
        elif notes_input == "3":
            text_input = input("введите ключевое слово: ")
            notes.search_notes(text_input)
        elif notes_input == "4":
            menu()
    if user_input == "3":
        text_input = input("введите ваше имя: ")
        print(info.greet(text_input))
        info.show_info()
    else:
        return


if __name__ == "__main__":
    menu()
