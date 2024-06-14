from Models.__init__ import CURSOR, CONN


class Branch:
    all = {}
    def __init__(self,name, branch_id = None, asset_balance = 0):
        self.branch_id = branch_id
        self.name = name
        self.asset_balance = asset_balance
        
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
                "Name must be a non-empty string"
            )

    @property
    def asset_balance(self):
        return self._asset_balance

    @asset_balance.setter
    def asset_balance(self, asset_balance):
        if isinstance(asset_balance, int): 
            self._asset_balance = asset_balance
        else:
            raise ValueError(
                "asset_balance must be a integer"
            )
### class methods
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of table instances """
        sql = """
            CREATE TABLE IF NOT EXISTS Branches (
            branch_id INTEGER PRIMARY KEY,
            name TEXT,
            asset_balance INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Department instances """
        sql = """
            DROP TABLE IF EXISTS Branches;
        """
        CURSOR.execute(sql)
        CONN.commit()

    

 ### crud methods
    ## create
    ## (new branch, new manager)
        ## new branch
    def create_branch(self):
        """ Insert a new row with the name and location values of the current Department instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO branches (name, asset_balance)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.asset_balance))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        ## new manager
            

    ## read
    ## asset_balance,all_branches

    ## update
    ## (fire_manager, new_manager)

    ## delete
    ##(close_branch, fire/release_manager )

    