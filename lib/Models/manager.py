from Models.__init__ import CONN, CURSOR
class Manager:
    def init(self, name, branch_assigned, employee_id = None):
        self.name = name
        self.branch_assigned = branch_assigned
        self.employee_id = employee_id
        self.accounts_managed = []


    @classmethod
    def create_table(cls):

        sql = """
            CREATE TABLE IF NOT EXISTS managers (
            employee_id INTEGER PRIMARY KEY,
            name TEXT,
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
 
        sql = """
            DROP TABLE IF EXISTS managers;
        """
        CURSOR.execute(sql)
        CONN.commit()
    def save(self):
  
        sql = """
            INSERT INTO managers (Name, Asset_balance)
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






@property
def account_managed(self):
 return [ account for account in bank.accounts if account["branch"] == self.branch_assigned]  

def query_users(self):
    for account in self.accounts_managed:
        print(f":Account Number: {account['account_number']}, Asset Balance: {account['asset_balance']}") 

def query_transactions(self):
    for transaction in bank.transaction:
        if transaction["account_number"] in [account["account_number"] for account in self.accounts_managed]:
           print(f"Account Number: {transaction['account_number']},Amount: {transaction['amount']},Transaction Type: {transaction['transactio_type']}")         

def get_branch_balance(self):
    total_balance = sum(account["asset_balance"] for account in self.account_managed)
    print(f"Branch Balance: {total_balance}")
    
def approve_loan(self, account_number, loan_amount):
    for account in bank.accounts:
        if account["account_number"] == account_number:
            account["balance"] += loan_amount
            print(f"Loan of {loan_amount} approved for account {account_number}")
            return
        print("Account not found")

def debit_account(self, account_number, loan_amount):
    for account in bank.accounts:
        if account["account_number"] ==account_number:
            if account["balance"] >= loan_amount:
                account["balance"] -= loan_amount
                print(f"debited {loan_amount} from account {account_number}")  
                return
            print("Insufficient balance")
            return
        print("Account not found")