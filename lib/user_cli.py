#!/usr/bin/env python3  

from user_helper import (
    exit,
    create_user,
    create_account,
    deposit_funds,
    check_balance,
    transfer_funds,
    withdraw_funds
)


def main():
     while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit()
            break
        elif choice == "1":
            create_user()
        elif choice == "2":
            create_account()
        elif choice == "3":
            deposit_funds()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            transfer_funds()
        elif choice == "6":
            withdraw_funds()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a User Account")
    print("2. Create a Bank Account")
    print("3. Deposit funds")
    print("4. Check balance")
    print("5. Withdraw funds")
   
  


if __name__ == "__main__":
    main()
