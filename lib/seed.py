#!/usr/bin/env python3
from Models.__init__ import CONN, CURSOR
from Models.branch import Branch
from Models.account  import Account
from Models.manager import Manager
from Models.user import User
from Models.transaction import Transaction

def seed_database():
    ## create tables
    Account.apply_loan(1,2000)
    pass


seed_database()
print("Seeded database")
