from Models.__init__ import CONN, CURSOR
from Models.transaction import Transaction
import sqlite3
from Models.__init__ import CONN, CURSOR

class Account:

    def __init__(self, account_id=None, user_id=None, branch_id=None, account_type=None, account_balance=0):
        self._account_id = account_id
        self.user_id = user_id   # INT FK
        self.branch_id = branch_id # INT FK
        self.account_type = account_type # TEXT
        self._account_balance = account_balance # FLOAT
<<<<<<< HEAD
        
    @classmethod
    def create_table(cls):

        sql = """
            CREATE TABLE IF NOT EXISTS Accounts (
            account_id INTEGER PRIMARY KEY,
            account_type TEXT,
            account_balance)
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

        self.branch_id = CURSOR.lastrowid
        type(self).all[self.branch_id] = self

    @classmethod
    def create(cls, name, password):
        """ Initialize a new Department instance and save the object to the database """
        branch = cls(name, password)
        branch.save()
        return branch


    
=======

>>>>>>> bdedd5ef9e3c96b5fdba8b298514190cc0ddcbdf
    
    @property
    def account_balance(self):
        return self._account_balance
    
    @property
    def account_id(self):
        return self._account_id
    
    @classmethod
    def create_table(cls):
        sql = """
              CREATE TABLE IF NOT EXISTS accounts (
              account_id INTEGER PRIMARY KEY AUTOINCREMENT,
              user_id INTEGER,
              branch_id INTEGER,
              account_type TEXT,
              account_balance FLOAT,
              FOREIGN KEY (user_id) REFERENCES users(user_id),
              FOREIGN KEY (branch_id) REFERENCES branches(branch_id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS accounts;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def save(cls, account):
        if not account.account_id:
            sql = """
               INSERT INTO accounts (user_id, branch_id, account_type, account_balance)
               VALUES (?,?,?,?)
            """
            CURSOR.execute(sql, (account.user_id, account.branch_id, account.account_type, account._account_balance))
            CONN.commit()
            account._account_id = CURSOR.lastrowid
        else:
            sql = """
                UPDATE accounts
                SET user_id=?, branch_id=?, account_type=?, account_balance=?
                WHERE account_id=?
            """
            CURSOR.execute(sql, (account.user_id, account.branch_id, account.account_type, account._account_balance, account.account_id))
            CONN.commit()

    @classmethod
    def create(cls, user_id, branch_id, account_type, initial_balance):
        account = cls(user_id=user_id, branch_id=branch_id, account_type=account_type, account_balance=initial_balance)
        cls.save(account)
        account.log_transaction('Deposit', initial_balance)
        return account
    
    @classmethod
    def get_by_id(cls, account_id):
        """ Get an Account instance from the database by account_id. """
        sql = """
            SELECT * FROM accounts WHERE account_id=?
        """
        CURSOR.execute(sql, (account_id,))
        row = CURSOR.fetchone()
        if row:
            account = cls(account_id=row[0], user_id=row[1], branch_id=row[2], account_type=row[3], account_balance=row[4])
            return account
        else:
            return None

    def deposit_account(self, amount):
        if amount > 0:
            self._account_balance += amount
            self.log_transaction('Deposit', amount)
            self.save()
        else:
            print(f"Invalid deposit amount: {amount}")

    def withdraw_account(self, amount):
        if amount <= self._account_balance:
            self._account_balance -= amount
            self.log_transaction('Withdrawal', amount)
            self.save()
            print(f'New balance: KSh{self._account_balance}')
        else:
            print(f"Invalid withdrawal amount: {amount}")

    def transfer_account(self, target_account, amount):
        if amount <= self._account_balance:
            self._account_balance -= amount
            target_account._account_balance += amount
            self.log_transaction('Transfer Out', amount, target_account.account_id, target_account.user_id)
            target_account.log_transaction('Transfer In', amount, self.account_id, self.user_id)
            self.save()
            target_account.save(target_account)
            print(f'New balance: KSh{self._account_balance}')
            print(f"Transfer of {amount} from account ID {self.account_id} to account ID {target_account.account_id} successful.")
        else:
            print(f"Insufficient balance to transfer {amount} from account ID {self.account_id}.")

    def log_transaction(self, transaction_type, amount, target_account_id=None, target_user_id=None):
        transaction = Transaction(
            account_id=self._account_id,
            user_id=self.user_id,
            transaction_type=transaction_type,
            amount=amount,
            balance=self._account_balance,
            target_account_id=target_account_id,
            target_user_id=target_user_id
        )
        transaction.add_transaction()



    def display_account_info(self):
        print(f"Account ID: {self.account_id}")
        print(f"User ID: {self.user_id}")
        print(f"Branch ID: {self.branch_id}")
        print(f"Account Type: {self.account_type}")
        print(f"Account Balance: {self.account_balance}")


