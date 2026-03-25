# Parent class(Родительский класс/суперкласс/базовый класс)
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

    def __repr__(self):
        read_status: str = "✅ Прочитана" if self.is_read else "❌ Не прочитана"
        return f"{self.title} - {self.author} | {self.pages} | {read_status}"

    def mark_as_read(self):
        self.is_read = True


# Child class(Дочерный класс/подкласс/субкласс)
class EBook(Book):
    file_size: float
    file_type: str

    def __init__(
        self,
        title: str,
        author: str,
        pages: int,
        file_size: float,
        file_type: str,
        is_read: bool = False,
    ):
        super().__init__(title, author, pages, is_read)
        self.file_size = file_size
        self.file_type = file_type

    def __repr__(self):
        return f"{super().__repr__()} | {self.file_size} MB | {self.file_type}"


class AudioBook(Book):
    duration_hours: float

    def __init__(
        self,
        title: str,
        author: str,
        pages: int,
        duration_hours: float,
        is_read: bool = False,
    ):
        super().__init__(title, author, pages, is_read)
        self.duration_hours = duration_hours

    def __repr__(self):
        return f"{super().__repr__()} | {self.duration_hours} часов"


# Полиморфизм(много форм)
def save_books(books: list[Book]) -> None:
    """
    Эта функция принимает любую книгу и записывает в library.txt
    """
    with open(file="./Урок 7/library.txt", mode="w") as file:
        for book in books:
            file.write(str(book) + "\n")


catalog = [
    Book("Властелин колец", "Толкин", 1200),
    EBook("Дюна", "Фрэнк Герберт", 412, 15.3, "pdf"),
    AudioBook("Гарри Поттер", "Роулинг", 500, 8.5),
]

save_books(catalog)

test = "asdf"
print(len(test))
print(len(catalog))

for item in catalog:
    print(item)
