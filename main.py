users = {
    "1234": {"balance": 1000},  # PIN: 1234, initial balance: $1000
    "5678": {"balance": 500}    # PIN: 5678, initial balance: $500
}

def authenticate_user():
    """Authenticate user based on PIN."""
    attempts = 3
    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ")
        if pin in users:
            print("Login successful.\n")
            return pin
        else:
            attempts -= 1
            print(f"Incorrect PIN. {attempts} attempt(s) remaining.\n")
    print("Too many failed attempts. Exiting.")
    return None

def show_menu():
    """Display the menu options."""
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def check_balance(pin):
    print(f"Your current balance is: ${users[pin]['balance']}")

def deposit_money(pin):
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid amount.")
        else:
            users[pin]['balance'] += amount
            print(f"${amount} deposited. New balance: ${users[pin]['balance']}")
    except ValueError:
        print("Please enter a valid number.")

def withdraw_money(pin):
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > users[pin]['balance']:
            print("Insufficient funds.")
        else:
            users[pin]['balance'] -= amount
            print(f"${amount} withdrawn. New balance: ${users[pin]['balance']}")
    except ValueError:
        print("Please enter a valid number.")

def atm_simulation():
    pin = authenticate_user()
    if not pin:
        return

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            check_balance(pin)
        elif choice == "2":
            deposit_money(pin)
        elif choice == "3":
            withdraw_money(pin)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the ATM simulation
atm_simulation()
