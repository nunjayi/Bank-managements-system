from Models.__init__ import CURSOR, CONN
from Models.transaction import Transaction
from Models.account import Account
from Models.user import User
from Models.branch import Branch
class Manager:
    all = {}
    def __init__(self,name, branch_id,employee_id = None,):
        self.employee_id = employee_id
        self.name = name
        self.branch_id = branch_id
        
    #### properties
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "name must be a non-empty string"
            )

    @property
    def branch_id(self):
        return self._branch_id

    @branch_id.setter
    def branch_id(self, branch_id):
        if isinstance(branch_id, int): 
            self._branch_id = branch_id
        else:
            raise ValueError(
                "branch_id must be a integer"
            )
        
    ## @classmethod
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of table instances """
        sql = """
            CREATE TABLE IF NOT EXISTS Managers (
            employee_id INTEGER PRIMARY KEY,
            name TEXT,
            branch_id INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()
##drop table
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Department instances """
        sql = """
            DROP TABLE IF EXISTS Managers;
        """
        CURSOR.execute(sql)
        CONN.commit()

    
    ### crud methods
    
    ## create
    ## (hire manager)
    def hire_manager(self):
        """ Insert a new row with the name and location values of the current Department instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO Managers (name, branch_id)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.branch_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    ## read
    def search_manager(self):
        pass

    ## account_info(to approve loans)
    ### 
    @classmethod
    def bank_balance(cls):
        credits = Transaction.credits()
        debits = Transaction.debits()
        asset_balance = credits - debits
        print(asset_balance)
        return asset_balance
    ## delete
    ##(fire/release_manager 