class Book:
    title: str
    author: str
    pages: int
    is_read: bool

    def __init__(
        self,
        title: str,
        author: str,
        pages: int,
        is_read: bool = False,
    ):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True

    def __repr__(self):
        read_status: str = "✅ Прочитана" if self.is_read else "❌ Не прочитана"
        return f"{self.title} - {self.author} | {self.pages} | {read_status}"


def save_books(books: list[Book]) -> None:
    with open(file="./Урок 6/library.txt", mode="w") as file:
        for book in books:
            file.write(f"{book.title}:{book.author}:{book.pages}:{book.is_read}\n")


def load_books() -> list:
    books = []
    with open(file="./Урок 6/library.txt", mode="r") as file:
        for line in file:
            title, author, pages, is_read = line.split(":")
            book = Book(
                title=title,
                author=author,
                pages=int(pages),
                is_read=is_read == "True",
            )
            books.append(book)

    return books


# Пример создания объекта
book = Book("Дюна", "Фрэнк Герберт", 412)
book2 = Book("Гарри Потер", "Д.Ж Роулинг", 500)
save_books([book, book2])
print(load_books())

zhantai = "Все понятно" or "Ничего не понятно"
