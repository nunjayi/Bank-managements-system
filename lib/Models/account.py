from Models.__init__ import CONN, CURSOR
from Models.transaction import Transaction

class Account:

    def __init__(self, account_id=None, user_id=None, branch_id=None, account_type=None, account_balance=0):
        self._account_id = Account.account_counter if account_id is None else account_id
        self.user_id = user_id   # INT FK
        self.branch_id = branch_id # INT FK
        self.account_type = account_type # TEXT
        self._account_balance = account_balance # FLOAT
        
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


    
    
    @property
    def account_balance(self):
        return self._account_balance
    
    @property
    def account_id(self):
        return self._account_id

    def deposit_account(self, amount):
        if amount > 0:
            self._account_balance += amount
            self.log_transaction('Deposit', amount)
        else:
            print(f"Invalid deposit amount: KSh{amount}")

    def withdraw_account(self, amount):
        if amount <= self._account_balance:
            self._account_balance -= amount
            self.log_transaction('Withdrawal', amount)
        else:
            print(f"Invalid withdrawal amount: KSh{amount}")

    def transfer_account(self, target_account, amount):
        if amount <= self._account_balance:
            self._account_balance -= amount
            target_account._account_balance += amount
            self.log_transaction('Transfer Out', amount, target_account.account_id, target_account.user_id)
            target_account.log_transaction('Transfer In', amount, self.account_id, self.user_id)
        else:
            print(f"Invalid transfer amount: KSh{amount}")

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