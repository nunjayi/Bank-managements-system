from transaction import Transaction

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