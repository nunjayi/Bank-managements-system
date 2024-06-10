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