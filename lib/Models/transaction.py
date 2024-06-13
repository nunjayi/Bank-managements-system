import datetime

class Transaction:
    transaction_counter = 1

    def __init__(self, account_id, user_id, transaction_type, amount, balance, target_user_id=None, target_account_id=None):
        self.transaction_id = Transaction.transaction_counter
        self.account_id = account_id
        self.user_id = user_id
        self.date = datetime.datetime.now()
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance
        self.target_user_id = target_user_id
        self.target_account_id = target_account_id
        Transaction.transaction_counter += 1

    def add_transaction(self):
        #add this to database
        if self.transaction_type == 'Transfer Out':
           print(f'New transaction: ID {self.transaction_id}\n'
                 f'Account {self.account_id} of User {self.user_id} has sent KSh{self.amount} to account {self.target_account_id} of User {self.target_user_id}\n'
                 f'Date: {self.date}\n'
                 f'New balance: KSh{self.balance}\n')
        elif self.transaction_type == 'Transfer In':
            print(f'New transaction: ID {self.transaction_id}\n'
                 f'Account {self.account_id} of User {self.user_id} has received KSh{self.amount} from Account {self.target_account_id} of User {self.target_user_id}\n'
                 f'Date: {self.date}\n'
                 f'New balance: KSh{self.balance}\n')
        elif self.transaction_type == 'Deposit':
           print(f'New transaction: ID {self.transaction_id}\n'
                 f'KSh{self.amount} has been deposited into Account {self.account_id} by User {self.user_id}\n'
                 f'Date: {self.date}\n'
                 f'New balance: KSh{self.balance}\n')
        elif self.transaction_type == 'Withdrawal':
           print(f'New transaction: ID {self.transaction_id}\n'
                 f'KSh{self.amount} has been withdrawn from Account {self.account_id} by User {self.user_id}\n'
                 f'Date: {self.date}\n'
                 f'New balance: KSh{self.balance}\n')