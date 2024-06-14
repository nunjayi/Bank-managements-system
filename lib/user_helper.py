#!/usr/bin/env python3

from Models.account import Account
from Models.user import User
def exit():
    print("Thank you! for visiting us.")


def create_user():
    name = input ("Enter the user's name: ")
<<<<<<< HEAD
    location = input("Enter the users's password: ")
=======
    password = input("Enter the user's password: ")
>>>>>>> bdedd5ef9e3c96b5fdba8b298514190cc0ddcbdf
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
    sender_account_id = input("Enter sender's account ID: ")
    receiver_account_id = input("Enter receiver's account ID: ")
    amount = float(input("Enter amount to transfer: "))
    transaction_id = input("Enter transaction ID: ")

    try:
        sender_account = Account.get(sender_account_id)
        receiver_account = Account.get(receiver_account_id)
        
        if not sender_account or not receiver_account:
            raise ValueError("Sender or receiver account not found")

        if sender_account.account_id == receiver_account.account_id:
            raise ValueError("Sender and receiver accounts cannot be the same")

        if sender_account.balance < amount:
            raise ValueError("Insufficient funds for transfer")

        sender_account.transfer_account(receiver_account, amount)
        print(f'Transaction ID: {transaction_id} - Transferred {amount} from {sender_account_id} to {receiver_account_id}')
        print(f'Transfer successful. Sender balance: {sender_account.balance}, Receiver balance: {receiver_account.balance}')
    
    except ValueError as ve:
        print(f"Error transferring funds: {ve}")
    
    except Exception as exc:
        print(f"Error transferring funds: {exc}")


def withdraw_funds():
    print('withdraw')
    pass

