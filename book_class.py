book_class.py
# book_class.py

class Book:
    """
    A class to represent a book, demonstrating Python's magic methods.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The publication year of the book.
    """
    def __init__(self, title: str, author: str, year: int):
        """
        The constructor (__init__) initializes a Book instance with title, author, and year.
        This is the magic method called when a new object is created.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' has been created.")

    def __del__(self):
        """
        The destructor (__del__) is called when an object's reference count drops to zero.
        It prints a message indicating the object is being deleted.
        """
        print(f"Deleting '{self.title}'...")

    def __str__(self) -> str:
        """
        The string representation method (__str__) returns a user-friendly string
        that is called by functions like print().
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """
        The official representation method (__repr__) returns a string that, if passed
        to eval(), could recreate the object. It's often used for debugging.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

# --- Example Usage ---
if __name__ == "__main__":
    # Create a Book object, which calls the __init__ method
    my_book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)

    # Print the object, which calls the __str__ method
    print("\nUser-friendly string representation:")
    print(my_book)

    # Get the official string representation, which calls the __repr__ method
    print("\nOfficial representation for debugging:")
    print(repr(my_book))

    # The __del__ method will be called when the script finishes and the object
    # goes out of scope, or you can explicitly delete it like this:
    print("\nExplicitly deleting the object...")
    del my_book
    print("Object deleted.")
    

   