#!/usr/bin/env python3

from Models.user import User
def exit():
    print("Thank you! for visiting us.")


# We'll implement the user functions in this lesson
def create_user():
    name = input ("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        user = User.create(name, location)
        print(f'Success: {user}')
    except Exception as exc:
        print("Error creating user: ", exc)

def create_account():

    pass

def deposit_funds():
    print('deposit')
    pass

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

