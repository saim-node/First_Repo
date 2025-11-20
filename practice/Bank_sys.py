# input name, account balance and deposit or withdraw amount 
# perform the operation and display the updated balance

user_name = input("Enter your name: ")
try:
    account_balance = float(input("Enter your account balance: "))
except ValueError:
    print("Invalid balance input.")
    exit()

operation = input("Do you want to deposit or withdraw? (d/w): ").lower()

if user_name == "" or account_balance < 0:
    print("Invalid input. Please enter a valid name or account balance.")
    exit()

# function
def print_account_info(balance, name, withdraw_amount=0, deposit_amount=0):
    print(f"\nAccount holder: {name}")
    if withdraw_amount > 0:
        print(f"Attempted withdrawal amount: {withdraw_amount}")
    elif deposit_amount > 0:
        print(f"Deposit amount: {deposit_amount}")
    print(f"Current balance: {balance}\n")

if operation == 'd':
    deposit_amount = float(input("Enter the amount to deposit: "))
    if deposit_amount <= 0:
        print("Deposit amount must be greater than 0.")
        exit()
    account_balance += deposit_amount
    print_account_info(account_balance, user_name, deposit_amount=deposit_amount)
    print("Deposit successful!")

elif operation == 'w':
    withdraw_amount = float(input("Enter the amount to withdraw: "))
    if withdraw_amount <= 0:
        print("Withdrawal amount must be greater than 0.")
        exit()
    if withdraw_amount > account_balance:
        print_account_info(account_balance, user_name, withdraw_amount=withdraw_amount)
        print("SORRY! Cannot withdraw more than the current balance.")
        exit()
    else:
        account_balance -= withdraw_amount
        print_account_info(account_balance, user_name, withdraw_amount=withdraw_amount)
        print("Withdrawal successful!")

else:
    print("Invalid operation. Please enter 'd' for deposit or 'w' for withdraw.")
