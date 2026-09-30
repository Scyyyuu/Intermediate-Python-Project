"""
Expense Tracker - a command-line app that saves your data to a JSON file.

Run:  python expense_tracker.py
"""
import json
from dataclasses import dataclass, asdict
from datetime import date
from pathlib import Path

DATA_FILE = Path(__file__).with_name("expenses.json")


@dataclass
class Expense:
    amount: float
    category: str
    description: str
    date: str  # stored as "YYYY-MM-DD"


class ExpenseTracker:
    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self.expenses = []
        self.load()

    # ---------- storage ----------
    def load(self):
        """Read expenses from the JSON file. No file yet? Start empty."""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.expenses = [Expense(**item) for item in json.load(f)]
        except FileNotFoundError:
            self.expenses = []
        except (json.JSONDecodeError, TypeError):
            print("Warning: data file is damaged. Starting with an empty list.")
            self.expenses = []

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([asdict(e) for e in self.expenses], f, indent=2)

    # ---------- actions ----------
    def add(self, amount, category, description, when=None):
        when = when or date.today().isoformat()
        self.expenses.append(Expense(amount, category.lower(), description, when))
        self.save()

    def delete(self, index):
        removed = self.expenses.pop(index)
        self.save()
        return removed

    def summary(self):
        """Return (totals_by_category, biggest_expense, grand_total)."""
        totals = {}
        for e in self.expenses:
            totals[e.category] = totals.get(e.category, 0) + e.amount
        biggest = max(self.expenses, key=lambda e: e.amount, default=None)
        return totals, biggest, sum(totals.values())


# ---------- user interface helpers ----------
def ask_amount():
    while True:
        raw = input("Amount: ").strip()
        try:
            value = float(raw)
            if value <= 0:
                print("  Amount must be greater than 0.")
                continue
            return value
        except ValueError:
            print("  Please enter a number, like 12.50")


def ask_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  This can't be empty.")


def ask_date():
    while True:
        raw = input("Date (YYYY-MM-DD, Enter for today): ").strip()
        if not raw:
            return date.today().isoformat()
        try:
            return date.fromisoformat(raw).isoformat()
        except ValueError:
            print("  Invalid date. Example: 2026-09-30")


def show_list(tracker):
    if not tracker.expenses:
        print("\nNo expenses yet.")
        return False
    print(f"\n{'#':<4}{'Date':<12}{'Category':<12}{'Amount':>10}  Description")
    print("-" * 56)
    for i, e in enumerate(tracker.expenses, start=1):
        print(f"{i:<4}{e.date:<12}{e.category:<12}{e.amount:>10.2f}  {e.description}")
    return True


def show_summary(tracker):
    if not tracker.expenses:
        print("\nNo expenses yet.")
        return
    totals, biggest, grand = tracker.summary()
    print("\nSpending by category")
    print("-" * 40)
    top = max(totals.values())
    for cat, total in sorted(totals.items(), key=lambda kv: kv[1], reverse=True):
        bar = "#" * max(1, int(20 * total / top))
        print(f"{cat:<12}{total:>10.2f}  {bar}")
    print("-" * 40)
    print(f"{'TOTAL':<12}{grand:>10.2f}")
    print(f"\nBiggest expense: {biggest.amount:.2f} on {biggest.category} "
          f"({biggest.description}, {biggest.date})")


def main():
    tracker = ExpenseTracker()
    menu = (
        "\n=== Expense Tracker ===\n"
        "1. Add expense\n"
        "2. List all expenses\n"
        "3. Summary\n"
        "4. Delete an expense\n"
        "5. Quit\n"
    )
    while True:
        print(menu)
        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            amount = ask_amount()
            category = ask_text("Category (food, transport, ...): ")
            description = ask_text("Description: ")
            when = ask_date()
            tracker.add(amount, category, description, when)
            print("Saved!")
        elif choice == "2":
            show_list(tracker)
        elif choice == "3":
            show_summary(tracker)
        elif choice == "4":
            if show_list(tracker):
                raw = input("\nNumber to delete (Enter to cancel): ").strip()
                if raw.isdigit() and 1 <= int(raw) <= len(tracker.expenses):
                    gone = tracker.delete(int(raw) - 1)
                    print(f"Deleted: {gone.description} ({gone.amount:.2f})")
                elif raw:
                    print("Invalid number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, 3, 4 or 5.")


if __name__ == "__main__":
    main()
