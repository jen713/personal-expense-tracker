import json
from datetime import datetime

def load_expenses(file_name='expenses.json'):
    """
    Loads expenses from a JSON file.
    If the file does not exist, it returns an empty list.
    """
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses, file_name='expenses.json'):
    """
    Saves the expenses to a JSON file.
    """
    with open(file_name, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """
    Prompts the user to enter expense details and adds them to the list.
    The date can be specified or defaults to the current date.
    """
    try:
        amount = float(input("Enter the amount: "))
        category = input("Enter the category (e.g., Food, Transport, Entertainment): ")
        date = input("Enter the date (YYYY-MM-DD) or leave blank for today: ")
        if not date:
            date = datetime.today().strftime('%Y-%m-%d')

        expenses.append({
            'amount': amount,
            'category': category,
            'date': date
        })

        save_expenses(expenses)
        print("Expense added successfully!")
    except ValueError:
        print("Error: Please enter a valid number for the amount.")

def view_summary(expenses):
    """
    Calculates and displays the total spending by category and overall.
    """
    category_totals = {}
    total_spent = 0

    for expense in expenses:
        total_spent += expense['amount']
        if expense['category'] in category_totals:
            category_totals[expense['category']] += expense['amount']
        else:
            category_totals[expense['category']] = expense['amount']

    print("\nTotal spending by category:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")

    print(f"\nTotal overall spending: ${total_spent:.2f}")

def main():
    """
    Main function that provides a user menu to add expenses, view summaries, or exit.
    """
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add an expense")
        print("2. View summaries")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
