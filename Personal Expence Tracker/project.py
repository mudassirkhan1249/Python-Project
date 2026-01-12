# Step 1: Global dictionary to store expenses
expenses = {
    'food': 0,
    'transportation': 0,
    'entertainment': 0,
    'utilities': 0,
}

def userExpense():
    while True:
        # Step 2: Take amount input
        try:
            amount = float(input("Enter the spent amount: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        # Step 3: Take category input
        category = input("Enter the category (food, transportation, entertainment, utilities): ").lower()
        if category not in expenses:
            print("Invalid category. Please choose from food, transportation, entertainment, utilities.")
            continue

        # Step 4: Update expense
        expenses[category] += amount
        print(f"Updated {category} expense: {expenses[category]}")

        # Step 5: Ask user if they want to continue
        choice = input("Do you want to add another expense? (yes/no): ").lower()
        if choice != 'yes':
            break

    # Step 6: Show summary
    print("\n--- Expense Summary ---")
    for cat, amt in expenses.items():
        print(f"{cat}: {amt}")
    total = sum(expenses.values())
    print(f"Total expense: {total}")

# Run the tracker
userExpense()
