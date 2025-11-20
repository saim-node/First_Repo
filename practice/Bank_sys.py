# input name, account balance  and deposit or withdraw amount 
# perform the operation and display the updated balance


user_name = input("Enter your name: ")
account_balance = float(input("Enter your account balance: "))
operation = input("Do you want to deposit or withdraw? (d/w): ").lower()

if user_name == "" or account_balance < 0:
    print("Invalid input. Please enter a valid name or account balance.")
    exit()

if operation == 'd':
    deposit_amount = float(input("Enter the amount to deposit: "))
    account_balance += deposit_amount
    print(f"Deposit successful! Updated balance for {user_name} is: ${account_balance:.2f}")

elif operation == 'w':
    withdraw_amount = float(input("Enter the amount to withdraw: "))
    if withdraw_amount > account_balance:
        print("withdraw successful! Updated balance for {user_name} is: {withdraw_amount:.2f}")
    else:
        account_balance -= withdraw_amount
        print(f"Withdrawal successful! Updated balance for {user_name} is: {account_balance:.2f}")
else:
    print("Invalid operation. Please enter 'd' for deposit or 'w' for withdraw.")