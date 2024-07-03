import json
import uuid


class ExpenseTracker:

    def __init__(self, file_name=None):
        if file_name:
            expenses_snapshot = self.load_expenses(file_name)
            print(expenses_snapshot)
            self.expenses = expenses_snapshot
        else:
            self.expenses = {}

    def load_expenses(self, file_name):
        with open(file_name, 'r') as fp:
            data = json.load(fp)
            return data

    def create_user(self, name):
        if name not in self.expenses:
            self.expenses[name] = {
                "groceries": 0.0, "travel": 0.0
            }
        return self.expenses[name]

    def add_expense(self, name, category, amount):
        if name not in self.expenses:
            return "User not found"
        user_expenses = self.expenses[name]
        if category not in user_expenses:
            return "Category not found"
        current_amount = user_expenses[category]
        print(f"Found Category {category} for user {name} with current amount before adding {current_amount}")
        current_amount += amount
        user_expenses[category] = current_amount
        return f" RETURN MESSAGE :: Added {amount} to {name}'s {category} category and current total is {current_amount}"

    def write_current_snapshot_to_file(self, file_name):
        with open(file_name, 'w') as fp:
            json.dump(self.expenses, fp)


def main():
    tracker = ExpenseTracker(file_name="expenses.json")
    tracker.create_user("sriraj")
    print(tracker.add_expense("sriraj", "groceries", 100))
    print(tracker.add_expense("sriraj", "groceries", 50))

    # tracker.write_current_snapshot_to_file(f"{uuid.uuid4()}_expenses.json")
    tracker.write_current_snapshot_to_file(f"expenses.json")


if __name__ == "__main__":
    main()
