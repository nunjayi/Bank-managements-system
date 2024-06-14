from Models.__init__ import CURSOR, CONN


class User:
    all = {}
    def __init__(self,name,password , branch_id,user_id = None,):
        self.user_id = user_id
        self.name = name
        self.password = password
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



    ### CLASS METHODS
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of table instances """
        sql = """
            CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY,
            name TEXT,
            password TEXT,
            branch_id INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Department instances """
        sql = """
            DROP TABLE IF EXISTS Users;
        """
        CURSOR.execute(sql)
        CONN.commit()

    ### crud methods

    ## create_user
    def create_user(self):
        """ Insert a new row with the name and location values of the current Department instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO Users(name, password,branch_id)
            VALUES (?, ? ,?)
        """

        CURSOR.execute(sql, (self.name, self.password,self.branch_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

        ##creating users
    @classmethod
    def create_user_account(cls, name, password, branch_id):
        """ Initialize a new Employee instance and save the object to the database """
        user = cls(name, password, branch_id)
        user.create_user()
        return user
    

    ## reading elements(find from db)
    @classmethod
    def instance_from_db(cls, row):
        """Return a user object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        user = cls.all.get(row[0])
        if user:
            # ensure attributes match row values in case local instance was modified
            user.name = row[1]
            user.password = row[2]
            user.Branch_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            user = cls(row[1], row[2],row[3])
            user.id = row[0]
            cls.all[user.id] = user
        return user

    ## search by id
    @classmethod
    def find_by_id(cls, id):
        """Return a user object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM Users
            WHERE user_id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        print(row)
        return cls.instance_from_db(row) if row else None