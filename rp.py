class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"ID: {self.book_id} | {self.title} by {self.author} | {status}"


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"ID: {self.patron_id} | Name: {self.name}"


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    # Add a new book
    def add_book(self, book):
        self.books[book.book_id] = book
        print(f'Book "{book.title}" added successfully.')

    # Register a patron
    def add_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f'Patron "{patron.name}" registered successfully.')

    # Issue a book
    def issue_book(self, book_id, patron_id):
        if book_id not in self.books:
            print("Book not found.")
            return

        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.is_issued:
            print("Book is already issued.")
        else:
            book.is_issued = True
            patron.borrowed_books.append(book)
            print(f'"{book.title}" issued to {patron.name}.')

    # Return a book
    def return_book(self, book_id, patron_id):
        if book_id not in self.books or patron_id not in self.patrons:
            print("Invalid Book ID or Patron ID.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book in patron.borrowed_books:
            patron.borrowed_books.remove(book)
            book.is_issued = False
            print(f'"{book.title}" returned successfully.')
        else:
            print("This patron did not borrow this book.")

    # Display all books
    def display_books(self):
        print("\nLibrary Books:")
        if not self.books:
            print("No books available.")
        else:
            for book in self.books.values():
                print(book)

    # Display all patrons
    def display_patrons(self):
        print("\nPatrons:")
        if not self.patrons:
            print("No patrons registered.")
        else:
            for patron in self.patrons.values():
                print(patron)

    # Display books borrowed by a patron
    def borrowed_books(self, patron_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        patron = self.patrons[patron_id]
        print(f"\nBooks borrowed by {patron.name}:")
        if not patron.borrowed_books:
            print("No books borrowed.")
        else:
            for book in patron.borrowed_books:
                print(book)


# ------------------- Main Program -------------------

library = Library()

# Add books
library.add_book(Book(101, "Python Programming", "John Smith"))
library.add_book(Book(102, "Data Structures", "Mark Allen"))
library.add_book(Book(103, "Machine Learning", "Andrew Ng"))

# Add patrons
library.add_patron(Patron(1, "Alice"))
library.add_patron(Patron(2, "Bob"))

# Display books
library.display_books()

# Issue books
library.issue_book(101, 1)
library.issue_book(102, 2)

# Display borrowed books
library.borrowed_books(1)
library.borrowed_books(2)

# Return a book
library.return_book(101, 1)

# Display books after return
library.display_books()