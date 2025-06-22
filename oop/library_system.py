# library_system.py

class Book:
    def __init__(self, title, author):
        """Initialize base Book with title and author"""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of Book"""
        return f"'{self.title}' by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook with additional file_size attribute"""
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def __str__(self):
        """String representation of EBook"""
        return f"{super().__str__()} [EBook, {self.file_size}KB]"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook with additional page_count attribute"""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation of PrintBook"""
        return f"{super().__str__()} [Print, {self.page_count} pages]"


class Library:
    def __init__(self):
        """Initialize Library with empty books list"""
        self.books = []

    def add_book(self, book):
        """Add a book to the library's collection"""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Can only add Book objects to the library")

    def list_books(self):
        """Print details of all books in the library"""
        print("Library Contents:")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")