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
    print("0. Join us. create user account:")
    print("1. open your bank account:")
    print("2. check your account balance:")
    print("3: deposit into your account:")
    print("4: withdraw from your account")
    print("5  send money")
    print("6: Apply for your loan")
    print("7  check your ministatement")
    print("8: Exit:")

   

if __name__ == "__main__":
    main()