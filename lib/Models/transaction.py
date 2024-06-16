from Models.__init__ import CURSOR, CONN

import datetime

class Transaction:
    all = {}
    def __init__(self,account_id,category,description,amount = 0,id = None ):
        self.id = id
        self.account_id = account_id
        self.category = category
        self.description = description
        self.amount = amount
        self.date= datetime.datetime.now()
 
    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        if isinstance(account_id, int):
            self._account_id = account_id
        else:
            raise ValueError(
                "account_id should be an integer"
            )

            
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if category == "debit" or "credit":
            self._category = category
        else:
            raise ValueError(
                " category can only be debit or credit "
            )
            
    
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if isinstance(amount, int):
            self._amount = amount
        else:
            raise ValueError(
                "amount is not an integer"
            )

        ###################333 CREATE OR DROP TABLE
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of transactions instances """
        sql = """
            CREATE TABLE IF NOT EXISTS Transactions(
            id INTEGER PRIMARY KEY,
            account_id INTEGER,
            category TEXT,
            description TEXT,
            amount INTEGER,
            date DATETIME)
        """
        CURSOR.execute(sql)
        CONN.commit()

        ##################### DROP TABLE
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Department instances """
        sql = """
            DROP TABLE IF EXISTS Transactions;
        """
        CURSOR.execute(sql)
        CONN.commit()
        ############################################## CREATE TRANSACTION
    def save(self):
        """ Insert a new row """
        sql = """
            INSERT INTO Transactions (account_id,category,description,amount,date)
            VALUES (?, ?,?,?,?)
        """

        CURSOR.execute(sql, (self.account_id, self.category,self.description,self.amount,self.date))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create_transaction(cls, account_id, category, description, amount):
        """ Initialize a new transaction instance and save the object to the database """
        transaction = cls(account_id, category, description, amount)
        transaction.save()
        return transaction
###############################3instance from db
    @classmethod
    def instance_from_db(cls, row):
        """Return a user object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        account = cls.all.get(row[0])
        if account:
            # ensure attributes match row values in case local instance was modified
            account.account_type = row[1]
            account.user_id = row[2]
            account.account_balance = row[3]
            account.account_created = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            account = cls(row[1], row[2],row[3],row[4])
            account.id = row[0]
            cls.all[account.id] = account
        return account



    ############# check you ministatement
    @classmethod
    def ministatement(cls,id):
        sql = """
            SELECT *
            FROM Transactions
            WHERE account_id = ?
        """
        rows = CURSOR.execute(sql, (id,)).fetchall()
        for row in rows:
            print(f"Transaction ID: {row[0]}\n"
                f"Account ID: {row[1]}\n"
                f"Description: {row[3]}\n"
                f"Amount: KSh{row[4]}\n"
                f"Date: {row[5]}\n")
        return [cls.instance_from_db(row) for row in rows]
            
###############################################################
    @classmethod
    def debits(cls):
        total = 0
        sql = """
            SELECT *
            FROM Transactions
            WHERE category = ?
        """
        rows = CURSOR.execute(sql, ("deposit",)).fetchall()
 
        for row in rows:
            total+=row[4]
        return total
    ##########################################################
    @classmethod
    def credits(cls):
        total = 0
        sql = """
            SELECT *
            FROM Transactions
            WHERE category = ?
        """
        rows = CURSOR.execute(sql, ("credit",)).fetchall()
        for row in rows:
            total+=row[4]
        return total







  