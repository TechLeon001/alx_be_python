class Book:
    """A class representing a book in the library system."""
    
    def __init__(self, title, author):
        """Initialize a book with title, author, and set it as available."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def __str__(self):
        """Return a string representation of the book."""
        return f"'{self.title}' by {self.author}"

    def check_out(self):
        """Check out the book if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize an empty library."""
        self._books = []  # Private list to store books

    def add_book(self, book):
        """Add a book to the library's collection."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only Book objects can be added to the library")

    def find_book(self, title):
        """Find a book by its title (case-insensitive)."""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def check_out_book(self, title):
        """Check out a book by title if available."""
        book = self.find_book(title)
        if book:
            if book.check_out():
                print(f"Successfully checked out: {book}")
            else:
                print(f"'{book.title}' is already checked out")
        else:
            print(f"Book not found: {title}")

    def return_book(self, title):
        """Return a book by title if it was checked out."""
        book = self.find_book(title)
        if book:
            if book.return_book():
                print(f"Successfully returned: {book}")
            else:
                print(f"'{book.title}' was not checked out")
        else:
            print(f"Book not found: {title}")

    def list_available_books(self):
        """List all currently available books."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available Books:")
            for book in available_books:
                print(f"- {book}")
        else:
            print("No books currently available")