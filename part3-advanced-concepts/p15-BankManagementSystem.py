from BankDatabase import *
from Bank import *
from Account import *
def main():
    database = BankDatabase()
    database.create_tables()
    bank = Bank(database)
    while True:
        print("\n================================")
        print("     BANK MANAGEMENT SYSTEM")
        print("================================")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")
        print("6. Transfer Money")
        print("7. Transaction History")
        print("8. Update Account")
        print("9. Close Account")
        print("10. Display All Accounts")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_no = int(input("Account Number: "))
            name = input("Customer Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            account_type = input("Account Type: ")
            balance = float(input("Initial Deposit: "))
            account = Account(
                account_no,
                name,
                email,
                phone,
                account_type,
                balance
            )
            print(account)
            bank.create_account(account)
        elif choice == "2":

            account_no = int(input("Account Number: "))

            bank.view_account(account_no)

        elif choice == "3":

            account_no = int(input("Account Number: "))
            amount = float(input("Deposit Amount: "))

            bank.deposit(account_no, amount)

        elif choice == "4":

            account_no = int(input("Account Number: "))
            amount = float(input("Withdrawal Amount: "))

            bank.withdraw(account_no, amount)

        elif choice == "5":

            account_no = int(input("Account Number: "))

            bank.check_balance(account_no)

        elif choice == "7":

            account_no = int(input("Account Number: "))

            bank.transaction_history(account_no)

        elif choice == "0":

            print("Thank you for using Bank Management System.")
            break

        else:
            print("Invalid choice.")



main()

