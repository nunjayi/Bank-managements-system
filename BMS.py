class Account:
    account_counter = 1000
    def __init__(self, account_type, deposit):
        self.account_type = account_type
        self.deposit = deposit
        self.balance = deposit
        self._account_id = Account.account_counter
        Account.account_counter += 1


    @property
    def account_balance(self):
        return self.balance
    
    @property
    def account_id(self):
        return self._account_id

class Branch:
    def __init__(self, branch_id, manager_id, name, asset_balance):
        self.branch_id = branch_id
        self.manager_id = manager_id
        self.name = name
        self.asset_balance = asset_balance
        self.accounts = []  # List to store Account objects
        self.users = []  # List to store User objects

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

    def __str__(self):
        return f"Branch(ID: {self.branch_id}, Name: {self.name}, Asset Balance: {self.asset_balance})"
