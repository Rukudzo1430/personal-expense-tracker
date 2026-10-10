import csv
import os

FILE_NAME = "expenses.csv"

# Load existing expenses
expenses = []

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expenses.append({
                "name": row["name"],
                "amount": float(row["amount"]),
                "category": row["category"]
            })

print("PERSONAL EXPENSE TRACKER")
print("------------------------")

while True:
    name = input(
        "Enter expense name (or 'done' to finish): "
    ).strip()

    if name.lower() == "done":
        break

    if not name:
        print("Expense name cannot be empty.")
        continue

    try:
        amount = float(input("Enter expense amount: "))

        if amount < 0:
            print("Amount cannot be negative.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    category = input(
        "Enter category (Food/Transport/Bills/Other): "
    ).strip()

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added successfully!\n")

# Save all expenses to CSV
with open(FILE_NAME, "w", newline="") as file:
    fieldnames = ["name", "amount", "category"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(expenses)

print("\nYOUR EXPENSES")
print("------------------------")

for expense in expenses:
    print(
        expense["name"],
        "|", expense["category"],
        "|", expense["amount"]
    )

total = sum(item["amount"] for item in expenses)

print("------------------------")
print("Total expenses:", round(total, 2))

print("\nSPENDING BY CATEGORY")
print("------------------------")

categories = {}

for expense in expenses:
    category = expense["category"] or "Uncategorised"
    categories[category] = (
        categories.get(category, 0) + expense["amount"]
    )

for category, amount in categories.items():
    print(category, ":", round(amount, 2))

print("\nExpenses saved to", FILE_NAME)