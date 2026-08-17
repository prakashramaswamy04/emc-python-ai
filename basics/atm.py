# Dictionary with 4 Users
users = {
    1111: {"name": "User 1", "balance": 5000},
    2222: {"name": "User 2", "balance": 10000},
    3333: {"name": "User 3", "balance": 7500},
    4444: {"name": "User 4", "balance": 15000}
}

print("=== Welcome to ATM ===")

for pin_attempt in range(1, 4):
    entered_pin = int(input("Enter your PIN: "))
    
    if entered_pin in users:
        user_data = users[entered_pin]
        user_name = user_data["name"]
        bank_balance = user_data["balance"]
        
        print(f"\nWelcome {user_name}. Your balance is ₹{bank_balance}")
        
        transaction_type = input("Choose operation (withdraw or deposit): ")
        
        if transaction_type == "withdraw":
            withdrawal_amount = int(input("Enter withdrawal amount: "))
            if bank_balance >= withdrawal_amount and withdrawal_amount > 0 and withdrawal_amount <= 10000:
                bank_balance = bank_balance - withdrawal_amount
                users[entered_pin]["balance"] = bank_balance
                print(f"Withdrawal successful! Balance after transaction: ₹{bank_balance}")
            elif withdrawal_amount > 10000:
                print("Maximum withdrawal per transaction = ₹10,000")
            else:
                print("Insufficient balance")
                
        elif transaction_type == "deposit":
            deposit_amount = int(input("Enter deposit amount: "))
            bank_balance = bank_balance + deposit_amount
            users[entered_pin]["balance"] = bank_balance
            print(f"Deposit successful! Balance after transaction: ₹{bank_balance}")
        else:
            print("Invalid Transaction")
        break
    else:
        print("Incorrect PIN")
        if pin_attempt == 3:
            print("Account Blocked")
            break