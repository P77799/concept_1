class Expense_tracker:
    def __init__(self):
        self.expenses = []

    def add_exp(self, amount, category):
        expense = {"category": category, "amount": amount}
        self.expenses.append(expense)
        print(f"Added category: {category} - Amount: {amount}")

    def views_expenses(self):
        if not self.expenses:
            print("No expenses yet!!")
        else:
            i = 1
            for ex in self.expenses:
                print(f"{i}. {ex['category']} - Rs.{ex['amount']}")
                i += 1

    def total_expenses(self):
        total = 0
        for ex in self.expenses:
            total += ex['amount']
        print(f"Total spent: Rs.{total}")


track = Expense_tracker()

while True:
    print("\n--- Expenses Tracker Menu ---")
    print("1. Add an expense")
    print("2. View expenses")
    print("3. View total spent")
    print("4. Exit")

    num = int(input("Enter num from 1-4: "))

    if num == 1:
        amount = int(input("Enter the amount: "))
        category = input("Enter the category: ")
        track.add_exp(amount, category)

    elif num == 2:
        track.views_expenses()

    elif num == 3:
        track.total_expenses()

    elif num == 4:
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")


