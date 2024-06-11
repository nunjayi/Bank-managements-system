class Account:
    account_counter = 1

    def __init__(self, account_id=None, user_id=None, branch_id=None, account_type=None, account_balance=0):
        self._account_id = Account.account_counter if account_id is None else account_id
        self.user_id = user_id   # INT FK
        self.branch_id = branch_id # INT FK
        self.account_type = account_type # TEXT
        self._account_balance = account_balance # FLOAT
        if account_id is None:
            Account.account_counter += 1
    
    @property
    def account_balance(self):
        return self._account_balance
    
    @property
    def account_id(self):
        return self._account_id

    def deposit_account(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited KSh{amount} to account {self.account_id}.")
            print(f"Your new balance: KSh{self.account_balance}")
        else:
            print(f"Invalid deposit amount: KSh{amount}")

    def withdraw_account(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrawn KSh{amount} from account {self.account_id}.")
            print(f"Your new balance: KSh{self.account_balance}")
        else:
            print(f"Invalid withdrawal amount: KSh{amount}")

    def transfer_account(self, target_account, amount):
        if amount > 0 and amount <= self._account_balance:
            self.withdraw_account(amount)
            target_account.deposit_account(amount)
            print(f"Transferred KSh{amount} from account {self.account_id} to account {target_account.account_id}.")
            print(f"KSh{self.account_balance} is your new account balance.")
        else:
            print(f"Invalid transfer amount: KSh{amount}")
