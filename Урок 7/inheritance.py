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


ebook = EBook(
    "Убийство в восточном экспрессе",
    "Agatha Christie",
    250,
    2500.0,
    "pdf",
)
ebook.mark_as_read()
print(ebook)
