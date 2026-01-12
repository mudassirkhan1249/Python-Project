import json
import os
import datetime

# ------------------------------
# Load data from JSON file safely
# ------------------------------
def load_data():
    if not os.path.exists("data.json"):  
        return []  
    with open("data.json", "r") as f:
        return json.load(f)

# ------------------------------
# Save data safely to JSON file
# ------------------------------
def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

# ------------------------------
# Add an expense
# ------------------------------
def add_expense():
    data = load_data()  # previous stored data list
    
    # Input amount
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            break
        except ValueError:
            print("Invalid amount! Please enter a numeric value.")
    
    # Category selection
    categories = ["Food", "Transport", "Utilities", "Entertainment", "Others"]
    print("\nSelect a category:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    
    while True:
        try:
            choice = int(input("Enter category number: "))
            if 1 <= choice <= len(categories):
                category = categories[choice - 1]
                break
            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Expense entry
    expense = {
        "Amount": amount,
        "Category": category,
        "Date": str(datetime.date.today())
    }
    
    data.append(expense)
    save_data(data)
    
    print("\n✔ Expense added successfully!")
    print(f"Amount: {amount}")
    print(f"Category: {category}")
    print(f"Date: {datetime.date.today()}")

# ------------------------------
# View all expenses
# ------------------------------
def view_expenses():
    data = load_data()
    
    if not data:
        print("\nNo expenses recorded yet.")
        return
    
    print("\n------ Your Saved Expenses ------")
    print(json.dumps(data, indent=4))

# ------------------------------
# Main menu loop
# ------------------------------
def main():
    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the app
main()
 