
import json
from datetime import date, timedelta

DATA_FILE = "library.json"
LOAN_DAYS = 7
FINE_PER_DAY = 5.0  # pesos per day overdue


class Book:
    def __init__(self, book_id, title, author, available=True):
        store the four values as attributes
        pass

    def to_dict(self):
        pass

    @staticmethod
    def from_dict(data)       
        pass

    def __str__(self):
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


class Library:
    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self.books = {}    # book_id -> Book
        self.members = {}  # member_id -> Member
        self.loans = []    # list of dicts: {"book_id", "member_id", "due_date"}
        self.load()

    def add_book(self, book_id, title, author):       
        pass

    def add_member(self, member_id, name):
        pass

    def search_books(self, keyword):        
        pass

    def borrow_book(self, book_id, member_id):
        pass

    def return_book(self, book_id):       
        pass

    def overdue_loans(self):
       
    def save(self):             
        pass

    def load(self):      
        pass


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
        # call the right Library method for each choice.
        # wrap each action in try/except so bad input never crashes the program.
        # call library.save() after any change.
        if choice == "7":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()