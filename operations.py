import data

def check_balance():
    print("Your balance is:", data.balance)

def deposit():
    amount = int(input("Enter amount to deposit: "))
    data.balance += amount
    print("Amount deposited successfully")

def withdraw():
    amount = int(input("Enter amount to withdraw: "))
    if amount > data.balance:
        print("Insufficient balance")
    else:
        data.balance -= amount
        print("Please collect your cash")