library_system.py
# library_system.py

class Book:
    """A base class for all types of books."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_details(self) -> str:
        """Returns a generic string representation of the book."""
        return f"Title: {self.title}, Author: {self.author}"

class EBook(Book):
    """A derived class for electronic books."""
    def __init__(self, title: str, author: str, file_size: int):
        # Call the constructor of the base class
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self) -> str:
        """Returns a detailed string for an EBook."""
        return f"{super().get_details()}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """A derived class for physical print books."""
    def __init__(self, title: str, author: str, page_count: int):
        # Call the constructor of the base class
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self) -> str:
        """Returns a detailed string for a PrintBook."""
        return f"{super().get_details()}, Page Count: {self.page_count}"

class Library:
    """
    Manages a collection of books, demonstrating composition.
    The library "has-a" list of books.
    """
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        """Adds any type of book (Book, EBook, or PrintBook) to the library."""
        self._books.append(book)
        print(f"Added '{book.title}' to the library.")

    def list_books(self):
        """
        Prints the details of each book in the library, using polymorphism
        to call the appropriate get_details method.
        """
        if not self._books:
            print("The library is currently empty.")
            return

        print("\n--- Current Library Collection ---")
        for book in self._books:
            print(book.get_details())
        print("----------------------------------")

# library_system.py

class Book:
    """A base class for all types of books."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_details(self) -> str:
        """Returns a generic string representation of the book."""
        return f"Title: {self.title}, Author: {self.author}"

class EBook(Book):
    """A derived class for electronic books."""
    def __init__(self, title: str, author: str, file_size: int):
        # Call the constructor of the base class
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self) -> str:
        """Returns a detailed string for an EBook."""
        return f"{super().get_details()}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """A derived class for physical print books."""
    def __init__(self, title: str, author: str, page_count: int):
        # Call the constructor of the base class
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self) -> str:
        """Returns a detailed string for a PrintBook."""
        return f"{super().get_details()}, Page Count: {self.page_count}"

class Library:
    """
    Manages a collection of books, demonstrating composition.
    The library "has-a" list of books.
    """
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        """Adds any type of book (Book, EBook, or PrintBook) to the library."""
        self._books.append(book)
        print(f"Added '{book.title}' to the library.")

    def list_books(self):
        """
        Prints the details of each book in the library, using polymorphism
        to call the appropriate get_details method.
        """
        if not self._books:
            print("The library is currently empty.")
            return

        print("\n--- Current Library Collection ---")
        for book in self._books:
            print(book.get_details())
        print("----------------------------------")

