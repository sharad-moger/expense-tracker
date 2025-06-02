class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description=""):
        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }
        self.expenses.append(expense)
        print("Expense added successfully.")

    def show_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        print("\nExpenses:")
        for i, exp in enumerate(self.expenses, 1):
            print(f"{i}. Amount: ₹{exp['amount']}, Category: {exp['category']}, Description: {exp['description']}")

    def total_expenses(self):
        total = sum(exp["amount"] for exp in self.expenses)
        print(f"\nTotal Expenses: ₹{total}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Show Total Expenses")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: ₹"))
                category = input("Enter category (e.g., Food, Transport): ")
                description = input("Enter description (optional): ")
                tracker.add_expense(amount, category, description)
            except ValueError:
                print("Invalid amount! Please enter a number.")
        elif choice == "2":
            tracker.show_expenses()
        elif choice == "3":
            tracker.total_expenses()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
3








