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
    name = input("Enter the user name > ")
    password = input("Enter the user password > ")
    branch_id = input("Enter the branch id > ")
    try:
        User.create_table()
        user = User.create_user_account(name,password,branch_id)
        print(f'Successfully created user with ID: {user.user_id}')
    except Exception as exc:
        print("Error creating user:", exc)
    pass
######################################## CREATE BANK ACCOUNT
def create_bank_account ():
    type = input("Enter the type of account (Savings , Checking) > ")
    user_id = input("Enter the user id > ")
    deposit = input("Enter your  first deposit > ")

    try:
        account = Account.create_user_account(type,int(user_id),int(deposit))
        print(f'Successfully created account ID {account.account_id} for User {user_id}')
    except Exception as exc:
        print("Error creating account: ", exc)

    
def account_balance():
    account_id = input("Enter your account id > ")
    Account.Check_balance(account_id)
    pass

def deposit_funds():

    id = input("Enter your account id > ")
    amount  = input("Enter the amount to deposit > ")
    if account := Account.find_by_id(id):
        try:
            
            account.asset_balance += int(amount)
            print(f"your previous balance was ->{account.asset_balance}")
            print(amount)
            account.deposit(account.asset_balance,int(amount),id)
            print(f'Success: {account}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Account {id} not found')

def withdraw_funds():
    
    id = input("Enter your account id > ")
    amount  = input("Enter the amount to withdraw > ")
    if account := Account.find_by_id(id):
        try:
           if account.asset_balance > int(amount):
                account.asset_balance -= int(amount)
                print(f"your previous balance was ->{account.asset_balance}")
                print(amount)
                account.withdraw(account.asset_balance,int(amount),id)
                print(f'Success: {account}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Account {id} not found')
    pass


def transfer_funds():

    ###enter details
    sender_id = input("Enter your account id - > ")
    send_amount = input("How much do you wish to send - > ")
    #sender id + amount
    receive_id = input("Send to ACCOUNT_ID - > ")
    ################ withdraw
    if a_sender_account := Account.find_by_id(sender_id):
        try:
           if a_sender_account.asset_balance > int(send_amount):
                a_sender_account.asset_balance -= int(send_amount)
                print(f"your previous balance was ->{a_sender_account.asset_balance}")
                a_sender_account.withdraw(a_sender_account.asset_balance,int(send_amount),sender_id)
                print(f'Success: {a_sender_account}')
        except Exception as exc:
            print("Error updating department: ", exc)
        
    else:
        print(f'Account {id} not found')
    
  ################## deposit
    #reciever
    if receive_account := Account.find_by_id(receive_id):
        try:
                
            receive_account.asset_balance += int(send_amount)
            print(f"sending {send_amount} to {receive_account}")
            receive_account.deposit(receive_account.asset_balance,int(send_amount),receive_id)
            print(f'Success: {receive_account}')
        except Exception as exc:
                print("Error updating department: ", exc)
        else:
            print(f'Account {id} not found')
    pass
def apply_loan():
    id = input("Enter your account id - > ")
    amount = input("How much do you want - > ")
    Account.apply_loan(id,amount)

    pass
def check_ministatement():
    id = input("Enter your account id - > ")
    Transaction.ministatement(id)