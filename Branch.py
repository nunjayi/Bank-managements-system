class Branch:
    def __init__(self, branch_id, manager_id, name, asset_balance):
        self.branch_id = branch_id
        self.manager_id = manager_id
        self.name = name
        self.asset_balance = asset_balance
        self.accounts = []
        self.users = []  

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

    def __str__(self):
        return f"Branch(ID: {self.branch_id}, Name: {self.name}, Asset Balance: {self.asset_balance})"
