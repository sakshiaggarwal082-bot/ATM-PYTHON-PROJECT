import data

def verify_pin():
    for i in range(3):   # 3 attempts
        pin = int(input("Enter your PIN: "))
        if pin == data.PIN:
            print("Login successful")
            return True
        else:
            print("Incorrect PIN")
    print("Too many attempts. Card blocked.")
    return False


def show_menu():
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def get_choice():
    return int(input("Enter your choice: "))