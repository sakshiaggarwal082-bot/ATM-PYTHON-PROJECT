import operations
import utils

if utils.verify_pin():   

    while True:
        utils.show_menu()
        choice = utils.get_choice()

        if choice == 1:
            operations.check_balance()
        elif choice == 2:
            operations.deposit()
        elif choice == 3:
            operations.withdraw()
        elif choice == 4:
            print("Thank you for using ATM")
            break
        else:
            print("Invalid choice")