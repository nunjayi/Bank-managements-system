from Models.transaction import Transaction

class Account:
    account_counter = 1

    def __init__(self, account_id=None, user_id=None, branch_id=None, account_type=None, account_balance=0):
        self._account_id = Account.account_counter if account_id is None else account_id
        self.user_id = user_id   # Assuming INT foreign key
        self.branch_id = branch_id  # Assuming INT foreign key
        self.account_type = account_type  # Assuming TEXT
        self._account_balance = account_balance  # Assuming FLOAT
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
            print(f"Invalid deposit amount: {amount}")

    def withdraw_account(self, amount):
        if amount <= self._account_balance:
            self._account_balance -= amount
            self.log_transaction('Withdrawal', amount)
        else:
            print(f"Invalid withdrawal amount: {amount}")

    def transfer_account(self, target_account, amount):
        if amount <= self._account_balance:
            self._account_balance -= amount
            target_account._account_balance += amount
            self.log_transaction('Transfer Out', amount, target_account.account_id, target_account.user_id)
            target_account.log_transaction('Transfer In', amount, self.account_id, self.user_id)
            print(f"Transfer of {amount} from account ID {self.account_id} to account ID {target_account.account_id} successful.")
        else:
            print(f"Insufficient balance to transfer {amount} from account ID {self.account_id}.")

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

    def display_account_info(self):
        print(f"Account ID: {self.account_id}")
        print(f"User ID: {self.user_id}")
        print(f"Branch ID: {self.branch_id}")
        print(f"Account Type: {self.account_type}")
        print(f"Account Balance: {self.account_balance}")


