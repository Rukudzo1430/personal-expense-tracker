expenses = [
    {"name": "Transport", "amount": 5.00},
    {"name": "Lunch", "amount": 8.50},
    {"name": "Groceries", "amount": 15.00},
    {"name": "Airtime", "amount": 3.00}
]

print("PERSONAL EXPENSE TRACKER")
print("------------------------")

for expense in expenses:
    print(expense["name"], ":", expense["amount"])

total = sum(expense["amount"] for expense in expenses)

print("------------------------")
print("Total expenses:", round(total, 2))