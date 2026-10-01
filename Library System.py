"""
Library Management System (CLI) - starter file
Run with: python library_system.py

Fill in every TODO. Read the HINT lines only if you get stuck.
"""

import json
from datetime import date, timedelta

DATA_FILE = "library.json"
LOAN_DAYS = 7
FINE_PER_DAY = 5.0  # pesos per day overdue


# ---------- Milestone 1: the building blocks ----------
class Book:
    def __init__(self, book_id, title, author, available=True):
        # TODO: store the four values as attributes
        pass

    def to_dict(self):
        """Return the book as a dictionary so it can be saved as JSON."""
        pass

    @staticmethod
    def from_dict(data):
        """Build a Book from a dictionary (the reverse of to_dict).
        HINT: Book(**data) works if the keys match the __init__ parameters.
        """
        pass

    def __str__(self):
        """TODO: return a nice one-line description, including Available / Borrowed.
        HINT: this is what print(book) will show.
        """
        pass


class Member:
    def __init__(self, member_id, name):
        # TODO: store id, name, and a list of borrowed book ids (starts empty)
        pass

    def to_dict(self):
        pass

    @staticmethod
    def from_dict(data):
        pass

    def __str__(self):
        pass


# ---------- Milestone 2: the library logic ----------
class Library:
    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self.books = {}    # book_id -> Book
        self.members = {}  # member_id -> Member
        self.loans = []    # list of dicts: {"book_id", "member_id", "due_date"}
        self.load()

    def add_book(self, book_id, title, author):
        """TODO: refuse duplicate ids (raise ValueError).
        HINT: dictionaries are fast for "does this key exist?" checks.
        """
        pass

    def add_member(self, member_id, name):
        pass

    def search_books(self, keyword):
        """Return all books whose title OR author contains the keyword.
        TODO: make it case-insensitive.
        HINT: .lower() and the `in` operator
        """
        pass

    def borrow_book(self, book_id, member_id):
        """TODO: check that the book and member exist, the book is available,
        and the member has fewer than 3 books. Then mark the book unavailable,
        record the loan with a due date, and update the member.
        HINT: str(date.today() + timedelta(days=LOAN_DAYS))
        """
        pass

    def return_book(self, book_id):
        """TODO: find the loan, mark the book available, remove the loan
        and the book from the member's list.
        Return the fine owed (0 if on time).
        HINT: date.fromisoformat(due_date) lets you compare with date.today()
        """
        pass

    def overdue_loans(self):
        """TODO: return every loan whose due date has already passed."""
        pass

    # ---------- Milestone 3: saving and loading ----------
    def save(self):
        """Write books, members, and loans into one JSON file.
        HINT: build one dict with three keys, using each object's to_dict().
        """
        pass

    def load(self):
        """Read the JSON file back into objects.
        TODO: if the file doesn't exist yet, start with empty data.
        """
        pass


# ---------- Milestone 4: the menu ----------
def show_menu():
    print("\n=== Library System ===")
    print("1. Add book")
    print("2. Add member")
    print("3. Search books")
    print("4. Borrow book")
    print("5. Return book")
    print("6. Show overdue loans")
    print("7. Quit")


def main():
    library = Library()
    while True:
        show_menu()
        choice = input("Choose: ").strip()
        # TODO: call the right Library method for each choice.
        # TODO: wrap each action in try/except so bad input never crashes the program.
        # TODO: call library.save() after any change.
        if choice == "7":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()