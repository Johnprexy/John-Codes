import random

users_account = {}

def generate_account_number():
    return random.randint(10001, 99999)

def create_account(username, password):
    # Create input for username and password and storing them in the dictionary.
    account_number = generate_account_number()
    users_account[account_number] = {'username': username, 'password': password, 'balance': 0}
    return f"Account created. Your account number is: {account_number}"

def deposit(account_number, amount):
    # Checking if the account_number exists in the dictionary and perform the deposit.
    if account_number in users_account:
        users_account[account_number]['balance'] += amount
        return f"Deposited ${amount}. New balance: ${users_account[account_number]['balance']}"
    else:
        return "Account not found."

def withdraw(account_number, amount):
    # Checking if the account_number exists in the dictionary and perform the withdrawal.
    if account_number in users_account:
        if users_account[account_number]['balance'] >= amount:
            users_account[account_number]['balance'] -= amount
            return f"Withdrew ${amount}. New balance: ${users_account[account_number]['balance']}"
        else:
            return "Insufficient funds."
    else:
        return "Account not found."
# While the functions defined up are correct, define functions that will initiate them
while True:
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")
    if choice == "1":
        # Input the username and password for account creation.
        username_input = input("Enter your username: ")
        password_input = input("Enter your password: ")
        print(create_account(username_input, password_input))
    elif choice == "2":
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter the deposit amount: "))
        print(deposit(account_number, amount))
    elif choice == "3":
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter the withdrawal amount: "))
        print(withdraw(account_number, amount))
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
