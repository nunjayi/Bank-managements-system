#!/usr/bin/env python3
from Models.__init__ import CONN, CURSOR
from Models.branch import Branch
from Models.account  import Account
from Models.manager import Manager
from Models.user import User
from Models.transaction import Transaction


def exit_program():
    print("Thank you for vsiting our office")
    exit()

def branch_balance():
    Manager.bank_balance()
    pass