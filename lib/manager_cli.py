#!/usr/bin/env python3
from manager_helper import (
    exit_program,
    branch_balance

    
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            branch_balance()
        elif choice == "1":
            exit_program()


def menu():
    print("                               ")
    print("WELCOME TO Managers Desk")
    print("                               ")
    print("MENU ->")
    print("                               ")
    print("0. bank_balance:")
    print("1. exit the menu:")


if __name__ == "__main__":
    main()