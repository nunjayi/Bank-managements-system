#!/usr/bin/env python3

from Models.account import Account
from Models.user import User
def exit():
    print("Thank you! for visiting us.")


def create_user():
    name = input ("Enter the user's name: ")
    password = input("Enter the user's password: ")
    try:
        user = User.create(name, password)
        user_id = user.user_id
        print(f'Successfully created user: {user_id}')
    except Exception as exc:
        print("Error creating user:", exc)

def create_account():
    user_id = input('Enter the user ID: ')
    branch_id = input('Enter the branch ID: ')
    account_type = input('Enter the account type: ')

    try:
        user = User.get_by_id(user_id)
        if not user:
            print(f"User with ID {user_id} not found")
            return
        
        initial_deposit = float(input('Enter the initial deposit amount (minimum KSh5000): '))
        if initial_deposit < 5000:
            print("Initial deposit must be at least KSh5000")
            return
        
        account = Account.create(user.user_id, branch_id, account_type, initial_deposit)
        print(f'Successfully created account ID {account.account_id} for User {user_id}.')
        print(f"Initial deposit of KSh{initial_deposit} successfully made.")

    except Exception as exc:
        print("Error creating account:", exc)

def deposit_funds():
    account_id = input('Enter your account ID: ')
    amount = float(input('Enter the amount to deposit: '))

    try:
        account = Account.get_by_id(account_id)
        if not account:
            print(f"Account with ID {account_id} not found")
            return
        
        account.deposit_account(amount)
        print (f'Successfully deposited KSh{amount} into account ID {account_id}')
    except Exception as exc:
        print("Error depositing funds:", exc)

def check_balance():
    print('balance')
    pass

def transfer_funds():
    print('transfer')
    pass

def withdraw_funds():
    print('withdraw')
    pass

