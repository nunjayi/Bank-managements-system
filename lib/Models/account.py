from Models.__init__ import CURSOR, CONN
from Models.transaction import Transaction

import datetime

class Account:
    all = {}
    def __init__(self,account_type,user_id,asset_balance,account_id = None, ):
        self.account_id = account_id
        self.account_type = account_type
        self.user_id = user_id
        self.asset_balance = asset_balance
        self.account_created= datetime.datetime.now()

       
        
    #### properties
    
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        if isinstance(account_type, str) and len(account_type):
            self._account_type = account_type
        else:
            raise ValueError(
                "account_type must be a non-empty string"
            )

    @property
    def asset_balance(self):
        return self._asset_balance

    @asset_balance.setter
    def asset_balance(self, asset_balance):
        if isinstance(asset_balance, int)and asset_balance>5000: 
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
            print(f"user id :{user_id}!")

            
    
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
    def Open_account(self):

        sql = """
            INSERT INTO Accounts(account_type ,user_id,asset_balance,account_created)
            VALUES (?, ?,? ,?)
        """

        CURSOR.execute(sql, (self.account_type, self.user_id,self.asset_balance,self.account_created))
        CONN.commit()

        self.account_id = CURSOR.lastrowid
        type(self).all[self.account_id] = self
        Transaction.create_transaction(self.account_id,"credit","deposit", self.asset_balance)
    @classmethod
    def create_user_account(cls, account_type, user_id,deposit):
        """ Initialize a new user bank account instance and save the object to the database """
        account = cls(account_type,user_id, deposit)
        account.Open_account()
        return account

################################## READ DATABASE
## CHECK BALANCE
    @classmethod
    def instance_from_db(cls, row):
        """Return a user object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        account = cls.all.get(row[0])
        print(type(row[0]))
        if account:
            # ensure attributes match row values in case local instance was modified
            account.account_type = row[1]
            account.user_id = row[2]
            account.account_balance = row[3]
            account.account_created = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            account = cls(row[1], row[2],row[3],row[4])
            cls.all[account.account_id] = account
        return account
    ####### FIND BY ID
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM Accounts
            WHERE account_id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        print(row)
        return cls.instance_from_db(row) if row else None




    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM Accounts
            WHERE account_id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        print(row)
        return cls.instance_from_db(row) if row else None

####### deposit
    def deposit(self,new_amount,deposit,id):
        sql = """
            UPDATE Accounts
            SET asset_balance= ?
            WHERE account_id = ?
        """
        CURSOR.execute(sql, (new_amount,id))
        CONN.commit()
        Transaction.create_transaction(self.account_id,"credit","deposit", deposit)
####### withdraw
    def withdraw(self,new_amount,deposit,id):
        sql = """
            UPDATE Accounts
            SET asset_balance= ?
            WHERE account_id = ?
        """
        CURSOR.execute(sql, (new_amount,id))
        CONN.commit()
        Transaction.create_transaction(self.account_id,"debit","withdraw", deposit)

    
    @classmethod
    def Check_balance(cls,id):
        """Return a user object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM Accounts
            WHERE account_id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        print(f" Your account balance is : {row[3]} Ksh Only")

        return row[3]
    
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
        print(f" Your account balance is : {row[3]} Ksh Only")

        return cls.instance_from_db(row) if row else None


################################################ DELETE FROM DATABASE
    @classmethod
    def apply_loan(cls, id,amount):
        balance = cls.Check_balance(id)
        limit = 0.60 * int(balance)
        if int(amount) < int(limit):
            print("approved")
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
            return True
        else:
            print("denied")
            return False




  