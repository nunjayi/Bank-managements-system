from Models.__init__ import CONN, CURSOR
class Branch:
    #all objects saved in the database
    all = {}
    def __init__(self, name,manager_id, branch_id = None,  asset_balance = 0):
        self.branch_id = branch_id
        self.manager_id = manager_id
        self.name = name
        self.asset_balance = asset_balance
        self.accounts = []
        self.users = []

    @classmethod
    def create_table(cls):

        sql = """
            CREATE TABLE IF NOT EXISTS branches (
            id INTEGER PRIMARY KEY,
            name TEXT,
            asset_balance REAL)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
 
        sql = """
            DROP TABLE IF EXISTS branches;
        """
        CURSOR.execute(sql)
        CONN.commit()
    def save(self):
  
        sql = """
            INSERT INTO branches (Name, Asset_balance)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.asset_balance))
        CONN.commit()

        self.branch_id = CURSOR.lastrowid
        type(self).all[self.branch_id] = self

    @classmethod
    def create(cls, name, asset_balance):
        """ Initialize a new Department instance and save the object to the database """
        branch = cls(name, asset_balance)
        branch.save()
        return branch



    

    def add_account(self, account):
        self.accounts.append(account)
        self.asset_balance += account.account_balance

    def remove_account(self, account_id):
        for account in self.accounts:
            if account.account_id == account_id:
                self.asset_balance -= account.account_balance
                self.accounts.remove(account)
                return True
        return False
    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                return True
        return False

    def query_account(self, account_id):
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        return None

    def query_balance(self, account_id):
        account = self.query_account(account_id)
        if account:
            return account.account_balance
        else:
            return None

    def calculate_total_asset_balance(self):
        total_balance = sum(account.account_balance for account in self.accounts)
        self.asset_balance = total_balance
        return self.asset_balance

    def update_asset_balance(self, account_id, transaction_type, amount):
        account = self.query_account(account_id)
        if not account:
            return False

        if transaction_type == 'deposit':
            account.deposit_account(amount)
            self.asset_balance += amount
        elif transaction_type == 'withdrawal':
            if account.withdraw_account(amount):
                self.asset_balance -= amount
            else:
                return False
        return True

    def get_asset_balance(self):
        return self.asset_balance

    def get_financial_summary(self):
        return {
            'branch_id': self.branch_id,
            'name': self.name,
            'total_asset_balance': self.asset_balance,
            'number_of_accounts': len(self.accounts)
        }

    def __str__(self):
        return f"Branch(ID: {self.branch_id}, Name: {self.name}, Asset Balance: {self.asset_balance})"
