import re
from Models.__init__ import CONN, CURSOR
from Models.branch import Branch
from Models.account  import Account
from Models.manager import Manager
from Models.user import User
from Models.transaction import Transaction

def exit_program():
    print("Thank you for transacting with us")
    exit()

def create_user():
    def format_name(name):
        return ' '.join(word.capitalize() for word in name.strip().split())
    
    def is_valid_password(password):
        return (
            len(password) >= 8 and
            re.search(r"[A-Z]", password) and
            re.search(r"[0-9]", password) and
            re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
        )
        
    name = input("Enter the user name > ")
    formatted_name = format_name(name)

    while True:
       password = input("Enter the user password > ")
       if is_valid_password(password):
           break
       else:
           print("Password must be at least 8 characters, contain at least one uppercase letter, one number, and one special character")

    branch_id = input("Enter the Branch ID > ")
    try:
        User.create_table()
        user = User.create_user_account(formatted_name, password, branch_id)
        print(f'Successfully created user with ID: {user.user_id}')
    except Exception as exc:
        print("Error creating user:", exc)

######################################## CREATE BANK ACCOUNT
def create_bank_account ():
    type = input("Enter the type of account (Savings , Checking) > ").strip().capitalize()
    user_id = input("Enter the User ID > ")
    deposit = input("Enter your  first deposit > ")

    try:
        account = Account.create_user_account(type, int(user_id), int(deposit))
        print(f'Successfully created Account ID {account.account_id} for User {user_id}')
    except Exception as exc:
        print("Error creating account: ", exc)
 
def account_balance():
    account_id = input("Enter your Account ID > ")

    try:
        account_id = int(account_id)
    except ValueError:
        print("Account ID must be an integer.")
        return
    try:
       Account.check_balance(account_id)
    except Exception as exc:
        print("Error checking balance: ", exc)

def deposit_funds():
    account_id = input("Enter your Account ID > ")
    amount  = input("Enter the amount to deposit > ")

    try:
        account_id = int(account_id)
        amount = int(amount)
    except ValueError:
        print("Account ID and deposit amount must be integers.")
        return
    
    account = Account.find_by_id(account_id)
    if account:
        try:
            account.deposit(amount)
            print (f'Successfully deposited KSh{amount} to Account ID {account_id}')
            print(f'New balance: KSh{account.asset_balance}')
        except Exception as exc:
            print("Error depositing funds: ", exc)
            
def withdraw_funds():    
    account_id = input("Enter your Account ID > ")
    amount  = input("Enter the amount to withdraw > ")

    try:
        account_id = int(account_id)
        amount = int(amount)
    except ValueError:
        print("Account ID and withdrawal amount must be integers.")
        return
        
    account = Account.find_by_id(account_id)
    if account:
        try:
            account.withdraw(amount)
            print (f'Successfully withdrew KSh{amount} from Account ID {account_id}')
            print(f'New balance: KSh{account.asset_balance}')
        except Exception as exc:
            print("Error withdrawing funds: ", exc)

def transfer_funds():

    ###enter details
    sender_id = input("Enter your Account ID > ")
    send_amount = input("How much do you wish to send > ")
    receiver_id = input("Send to Account ID > ")
    ################ withdraw
    
    try:
        sender_id = int(sender_id)
        send_amount = int(send_amount)
        receiver_id = int(receiver_id)
    except ValueError:
        print("Account ID and amount must be integers.")
        return
    
    sender_account = Account.find_by_id(sender_id)
    receiver_account = Account.find_by_id(receiver_id)

    if not sender_account or not receiver_account:
        print ("Invalid account ID(s)")
        return
        
    try:
       if sender_account.asset_balance >= send_amount:
        sender_account.withdraw(send_amount)
        receiver_account.deposit(send_amount)
        print (f'Successfully transferred KSh{send_amount} from Account ID {sender_id} to Account ID {receiver_id}')
        print(f'New balance: KSh{sender_account.asset_balance}')
       else:
           print("Insufficient funds")
    except Exception as exc:
        print("Error transferring funds: ", exc)

def apply_loan():
    account_id = input("Enter your Account ID > ")
    amount = input("How much do you want > ")
    
    try:
        account_id = int(account_id)
        amount = int(amount)
    except ValueError:
        print("Account ID and loan amount must be integers.")
        return
    
    try:
        Account.apply_loan(account_id, amount)
        print(f'Successfully applied for a loan of KSh{amount} for Account ID {account_id}')
    except Exception as exc:
        print("Error applying loan: ", exc)

def check_ministatement():
    account_id = input("Enter your Account ID > ")

    try:
        account_id = int(account_id)
    except ValueError:
        print("Account ID must be an integer.")
        return
    
    account = Account.find_by_id(account_id)
    if account:
        Transaction.ministatement(account_id)
    else:
        print("Account ID not found")
    