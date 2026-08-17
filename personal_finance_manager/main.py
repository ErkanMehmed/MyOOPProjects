from personal_finance_manager.user import User
from personal_finance_manager.wallet import Wallet


def print_menu():
    print("\n" + "=" * 30)
    print("Personal Finance Manager")
    print("=" * 30)
    print("1. Create User")
    print("2. Add income / expense")
    print("3. View balance")
    print("4. View transaction history")
    print("5. Exit")
    print("=" * 30)


def main():
    wallet = None

    while True:
        print_menu()
        choice = input("Please choose a number from 1 to 5: ").strip()

        if choice == '1':
            print("\n--- Create user ---")
            try:
                first_name = input("Name: ")
                last_name = input("Last name: ")
                age = int(input("Age: "))
                city = input("City: ")
                address = input("Address (For example - Sofia123): ")
                budget = float(input("Your Budget: "))

                user = User(first_name, last_name, age, city, address, budget)

                monthly_limit = input("Enter a monthly spending limit (or 0 if there is none): ")
                monthly_limit = float(monthly_limit) if monthly_limit else 0.0

                wallet = Wallet(user, monthly_limit)
                print(f"User {user.first_name} {user.last_name} has been created successfully!")

            except ValueError as e:
                print(f"Input error: {e}")

        elif choice == '2':
            if not wallet:
                print("First, you need to create a user (Option 1)!")
                continue

            print("\n--- Add transaction ---")
            trans_type = input("Type (Income / Expense): ").strip().capitalize()

            if trans_type not in ["Income", "Expense"]:
                print("Invalid transaction type! Please enter 'Income' or 'Expense'.")
                continue

            try:
                amount = float(input("Amount: "))
                category = input("Category (e.g. Food, Salary): ")
                merchant = input("Merchant: ")

                result = wallet.add_transaction(amount, category, merchant, trans_type)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '3':
            if not wallet:
                print("First, you need to create a user (Option 1)!")
                continue

            print("\n--- Current Balance ---")
            print(f"Available Budget: {wallet.get_current_budget():.2f} лв.")
            if wallet.monthly_limit > 0:
                print(
                    f"Spent this month: {wallet.get_current_month_expenses():.2f} / {wallet.monthly_limit:.2f} лв.")

        elif choice == '4':
            if not wallet:
                print("First, you need to create a user (Option 1)!")
                continue

            print("\n--- Transaction History ---")
            history = wallet.get_history_transactions()
            print(history)

            print("\n--- Summary ---")
            print(wallet.get_summary())

        elif choice == '5':
            print("Goodbye! Thank you for using Personal Finance Manager.")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()