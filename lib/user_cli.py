#!/usr/bin/env python3
from user_helper import (
    exit_program,
    create_user,
    create_bank_account,
    account_balance,
    deposit_funds,
    withdraw_funds,
    apply_loan,
    transfer_funds,
    check_ministatement
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            create_user()
        elif choice == "1":
            create_bank_account()
        elif choice == "2":
            account_balance()
        elif choice == "3":
            deposit_funds()
        elif choice == "4":
            withdraw_funds()
        elif choice == "5":
            transfer_funds()
        elif choice == "6":
            apply_loan()
        elif choice == "7"   :
            check_ministatement()
        elif choice == "8":
            exit_program()
        else:
            menu()
            print("               ")
            print("!!!!!!!!!!!!!!!")
            print("invalid input")
        


def menu():
    print("                               ")
    print("WELCOME TO JAMII BANK")
    print("                               ")
    print("User MENU ->")
    print("                               ")
    print("0. Join us. Create a User Account")
    print("1. Open your Bank Account")
    print("2. Check your Account Balance")
    print("3: Deposit into your Account")
    print("4: Withdraw from your Account")
    print("5  Send Money")
    print("6: Apply for your Loan")
    print("7  Check your Ministatement")
    print("8: Exit:")

   

if __name__ == "__main__":
    main()