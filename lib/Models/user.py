from datetime import datetime
import sqlite3
from Models.__init__ import CONN, CURSOR
from Models.account import Account
from Models.transaction import Transaction

class User:
    def __init__(self, name, password, user_id=None):
        self._user_id = user_id
        self.name = name
        self.password = password
        self.accounts = []
        self.loans = []
        

    @property
    def user_id(self):
        return self._user_id    

    @classmethod
    def create_table(cls):

        sql = """
            CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            name TEXT,
            password TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
 
        sql = """
            DROP TABLE IF EXISTS users;
        """
        CURSOR.execute(sql)
        CONN.commit()
    def save(self):
  
        sql = """
            INSERT INTO users (name, password)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.password))
        CONN.commit()
        self._user_id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, password):
        """ Initialize a new Department instance and save the object to the database """
        user = cls(name, password)
        user.save()
        return user  
    
    @classmethod
    def get_by_id(cls, user_id):
        """ Get a User instance from the database """
        sql = """
            SELECT * FROM users WHERE user_id =?
        """
        CURSOR.execute(sql, (user_id,))
        row = CURSOR.fetchone()
        if row:
            user = cls(row[1], row[2], row[0])
            return user
        else:
            return None

    def open_account(self, account_type, initial_deposit):
        account = Account.create(self.user_id, branch_id=None, account_type=account_type, initial_balance=initial_deposit)
        self.accounts.append(account)
        print(f"Account with ID {account.account_id} and Account No {account.account_no} opened for {self.name} with balance {account.balance}")

    def close_account(self, account_id):
        account_to_close = next((acct for acct in self.accounts if acct.account_id == account_id), None)
        if account_to_close:
            self.accounts.remove(account_to_close)
            print(f"Account with ID {account_id} closed for {self.name}")
        else:
            print(f"Account with ID {account_id} not found")

    def deposit(self, account_id, amount):
        account = next((acct for acct in self.accounts if acct.account_id == account_id), None)
        if account:
            account.balance += amount
            print(f"Deposited {amount} to account ID {account_id}. New balance: {account.balance}")
        else:
            print(f"Account with ID {account_id} not found")

    def withdraw(self, account_id, amount):
        account = next((acct for acct in self.accounts if acct.account_id == account_id), None)
        if account:
            if account.balance >= amount:
                account.balance -= amount
                print(f"Withdrew {amount} from account ID {account_id}. New balance: {account.balance}")
            else:
                print("Insufficient funds")
        else:
            print(f"Account with ID {account_id} not found")

    def check_balance(self, account_id):
        account = next((acct for acct in self.accounts if acct.account_id == account_id), None)
        if account:
            print(f"Balance for account ID {account_id} is {account.balance}")
            return account.balance
        else:
            print(f"Account with ID {account_id} not found")
            return None

    def transfer(self, source_account_id, target_account_id, amount):
        source_account = next((acct for acct in self.accounts if acct.account_id == source_account_id), None)
        target_account = next((acct for acct in self.accounts if acct.account_id == target_account_id), None)
        if source_account and target_account:
            if source_account.balance >= amount:
                source_account.balance -= amount
                target_account.balance += amount
                print(f"Transferred {amount} from account ID {source_account_id} to account ID {target_account_id}")
            else:
                print("Insufficient funds")
        else:
            if not source_account:
                print(f"Source account with ID {source_account_id} not found")
            if not target_account:
                print(f"Target account with ID {target_account_id} not found")

    def apply_loan(self, loan_amount):
        self.loans.append(loan_amount)
        print(f"Loan of {loan_amount} applied for {self.name}")
