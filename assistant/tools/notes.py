from datetime import datetime


def add_note(text: str) -> None:
    now = datetime.now()
    formatted_time = now.strftime("%d.%m.%Y")

    with open("./assistant/tools/notes.txt", "a") as file:
        file.write(f"{formatted_time} {text}\n")


def load_notes() -> list[str]:
    notes = []

    try:
        with open("./assistant/tools/notes.txt") as file:
            for note in file:
                notes.append(note)
    except Exception:
        pass

    return notes


def show_notes() -> None:
    notes = load_notes()

    if len(notes) == 0:
        print("Заметок пока нет")
        return

    for index, note in enumerate(notes, 1):
        print(f"{index}. {note}")


def search_notes(keyword: str) -> None:
    notes = load_notes()

    if len(notes) == 0:
        print("Заметок пока нет")
        return

    found = False
    for index, note in enumerate(notes, 1):
        if keyword in note:
            found = True
            print(f"{index}. {note}")

    if not found:
        print("Ничего не найдено")
