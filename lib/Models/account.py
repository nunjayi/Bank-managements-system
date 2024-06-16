from Models.__init__ import CURSOR, CONN
from Models.transaction import Transaction
import datetime

class Account:
    all = {}
    def __init__(self, account_type, user_id, asset_balance, account_id=None):
        self.account_id = account_id
        self.account_type = account_type
        self.user_id = user_id
        self.asset_balance = asset_balance
        self.account_created = datetime.datetime.now()

    #### properties
    
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        if isinstance(account_type, str) and len(account_type):
            self._account_type = account_type
        else:
            raise ValueError("account_type must be a non-empty string")

    @property
    def asset_balance(self):
        return self._asset_balance

    @asset_balance.setter
    def asset_balance(self, asset_balance):
        if isinstance(asset_balance, int) and asset_balance > 5000: 
            self._asset_balance = asset_balance
        else:
            print("deposit must be above 5000")
            
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        if isinstance(user_id, int): 
            self._user_id = int(user_id)          
        else:
           raise ValueError("User ID must be an integer")
  
    
    ### CLASS MEHTODS
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of table instances """
        sql = """
            CREATE TABLE IF NOT EXISTS Accounts (
            account_id INTEGER PRIMARY KEY,
            account_type TEXT,
            user_id INTEGER,
            asset_balance INTEGER,
            account_created DATETIME)
        """
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Department instances """
        sql = """
            DROP TABLE IF EXISTS Accounts;
        """
        CURSOR.execute(sql)
        CONN.commit()

    ### crud methods
      ## Open_account
    def open_account(self):
        sql = """
            INSERT INTO Accounts(account_type ,user_id,asset_balance,account_created)
            VALUES (?, ?,? ,?)
        """
        CURSOR.execute(sql, (self.account_type, self.user_id, self.asset_balance, self.account_created))
        CONN.commit()

        self.account_id = CURSOR.lastrowid
        type(self).all[self.account_id] = self
        Transaction.create_transaction(self.account_id, "credit", "deposit", self.asset_balance)
    @classmethod
    def create_user_account(cls, account_type, user_id, deposit):
        """ Initialize a new user bank account instance and save the object to the database """
        account = cls(account_type, user_id, deposit)
        account.open_account()
        return account

################################## READ DATABASE
## CHECK BALANCE
    @classmethod
    def instance_from_db(cls, row):
        """Return an account object having the attribute values from the table row."""
        account_id = row[0]
        account_type = row[1]
        user_id = row[2]
        asset_balance = row[3]
        account_created = row[4]

        account = cls.all.get(account_id)
        if account:
            account.account_type = account_type
            account.user_id = user_id
            account.asset_balance = asset_balance
            account.account_created = account_created
        else:
            account = cls(account_type, user_id, asset_balance, account_id)
            cls.all[account_id] = account
        return account
    ####### FIND BY ID
    @classmethod
    def find_by_id(cls, account_id):
        sql = """
            SELECT *
            FROM Accounts
            WHERE account_id = ?
        """
        row = CURSOR.execute(sql, (account_id,)).fetchone()
        print(row)
        return cls.instance_from_db(row) if row else None

####### deposit
    def deposit(self, deposit_amount):
        if not isinstance(deposit_amount, int):
            raise TypeError("Deposit amount should be an integer")
        
        new_balance= self.asset_balance + deposit_amount
        sql = """
            UPDATE Accounts
            SET asset_balance= ?
            WHERE account_id = ?
        """
        CURSOR.execute(sql, (new_balance, self.account_id))
        CONN.commit()
        self.asset_balance = new_balance
        Transaction.create_transaction(self.account_id, "credit", "deposit", deposit_amount)

####### withdraw
    def withdraw(self, withdrawal_amount):
       if not isinstance(withdrawal_amount, int):
          raise TypeError("Withdrawal amount should be an integers")
       
       if self.asset_balance >= withdrawal_amount:
           new_balance = self.asset_balance - withdrawal_amount
           sql = """
               UPDATE Accounts
               SET asset_balance =?
               WHERE account_id =?
           """
           CURSOR.execute(sql, (new_balance, self.account_id))
           CONN.commit()
           self.asset_balance = new_balance
           Transaction.create_transaction(self.account_id, "debit", "withdrawal", withdrawal_amount)
       else:
            raise ValueError("Insufficient Balance")
    
    @classmethod
    def check_balance(cls, account_id):
        """Return a user object corresponding to the table row matching the specified primary key"""
        account = cls.find_by_id(account_id)
        if not account:
            raise ValueError("Incorrect ID")
                
        sql = """
            SELECT asset_balance
            FROM Accounts
            WHERE account_id = ?
        """
        row = CURSOR.execute(sql, (account_id,)).fetchone()
        print(f" Your account balance is: Ksh{row[0]} Only")
        return row[0]
        
################################################# UPDATE DATABASE
    @classmethod
    def create_deposit(cls,id):
        """Return a user object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM Accounts
            WHERE account_id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        print(f" Your account balance is: KSh{row[3]} Only")
        return cls.instance_from_db(row) if row else None

################################################ DELETE FROM DATABASE
    @classmethod
    def apply_loan(cls, account_id, amount):
        account = cls.find_by_id(account_id)
        current_balance = account.asset_balance
        loan_limit = 0.60 * current_balance

        if amount <= loan_limit:
            account.deposit(amount)
            print(f"Loan approved. Your new balance is: KSh{account.asset_balance}")
            return True
        else:
            print("Loan denied. Amount exceeds loan limit.")
            return False
       