# Base class - Book
class Book:
    def __init__(self, title, author):
        """Initialize title and author for a book."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for Book."""
        return f"Book: {self.title} by {self.author}"


# Derived class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an EBook with file size."""
        super().__init__(title, author)  # Call base class constructor
        self.file_size = file_size

    def __str__(self):
        """String representation for EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook with page count."""
        super().__init__(title, author)  # Call base class constructor
        self.page_count = page_count

    def __str__(self):
        """String representation for PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Library class (demonstrating composition)
class Library:
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library collection."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library with their details."""
        for book in self.books:
            print(book)
